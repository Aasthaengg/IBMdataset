N, T = list(map(int,input().split()))
t = list(map(int,input().split()))
s = T
for i in range(1,N):
    s += t[i]+T - max(t[i],t[i-1]+T)
print(s)