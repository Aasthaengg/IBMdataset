import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


s = input()
n = len(s)
ans = []
l = []
i = 0
pi = 0
def sub(pi,i,point):
    l = [0]*(i-pi)
    l[point-pi] = (point-pi)//2 + (i-point-1)//2 + 1
    l[point-1-pi] = (i-pi) - l[point-pi]
    return l
while i<n:
    while i<n and s[i]=="R":
        i += 1
    point = i
    while i<n and s[i]=="L":
        i += 1
    l.extend(sub(pi,i,point))
#     print(l, pi, i, point)
    pi = i
write(" ".join(map(str, l)))