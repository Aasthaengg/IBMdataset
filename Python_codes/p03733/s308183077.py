n,T = map(int,input().split())	
t = list(map(int,input().split()))
minus=0
for i in range(n-1):
    if t[i+1]-t[i]<T:
        minus+=T-t[i+1]+t[i]
print(n*T-minus)



