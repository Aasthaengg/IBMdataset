N,X,T = map(int,input().split())
k = N/X
t = N//X
if k > t:
    print((t+1)*T)
else:
    print(t*T)