import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


s = input()
x,y = map(int, input().split())

xs = []
ys = []
isx = True
i = 0
n = len(s)
while i<n and s[i]=="F":
    x -= 1
    i += 1

while i<n:
    c = 0
    while i<n and s[i]=="F":
        i += 1
        c += 1
    if isx and c>0:
        xs.append(c)
    elif c>0:
        ys.append(c)
    isx = not isx
    i += 1
    
def sub(l, target):
    # lの一部の符号を反転してtargetを作れるか
    val = sum(l)
    prev = [False] * (2*(val+1))
    prev[val] = True
    current = None
    for num in l:
        current = [False] * (2*(val+1))
        for i in range(2*(val+1)):
            if i-num>=0 and prev[i-num]:
                current[i] = True
            if i+num<(2*val+2) and prev[i+num]:
                current[i] = True
        prev = current
    if current is None:
        current = prev
    return current[target+val]

if sum(abs(item) for item in xs)>=abs(x) and sum(abs(item) for item in ys)>=abs(y) and sub(xs, x) and sub(ys, y):
    print("Yes")
else:
    print("No")