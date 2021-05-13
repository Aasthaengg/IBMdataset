N = int(input())
s = [input() for i in range(N)]
M = int(input())
t = [input() for i in range(M)]
a=[0]*101
for i in range(N):
    a[i]=s.count(s[i])
    for j in range(M):
        if s[i]==t[j]:
            a[i]-=1

print(max(a))