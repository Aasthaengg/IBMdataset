def LI(): return list(map(int,input().split()))
N,T = LI()
t = LI()
ans =N*T
for i in range(N-1):
    if t[i+1]-t[i]<T:
        ans -= T-(t[i+1]-t[i])
print(ans)
