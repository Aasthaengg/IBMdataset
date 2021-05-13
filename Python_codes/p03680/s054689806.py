import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n = int(input())
a = [None]*n
for i in range(n):
    a[i] = int(input())-1
s = set()
c = 0
while True:
#     print(c)
    if c in s:
        ans = -1
        break
    s.add(c)
    c = a[c]
    if c==1:
        ans = len(s)
        break
print(ans)