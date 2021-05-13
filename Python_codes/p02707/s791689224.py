import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n = int(input())
a = list(map(int, input().split()))
d = {i:[] for i in range(1,n+1)}
for i,num in enumerate(a):
    d[num].append(i+2)
ans = []
for i in range(1,n+1):
    ans.append(len(d[i]))
write("\n".join(map(str, ans)))