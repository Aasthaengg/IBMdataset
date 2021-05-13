#17
n,T = map(int,input().split())
t = list(map(int,input().split()))
Sum = T

for i in range(n-1):
    if t[i+1]-t[i]<T:
        Sum += t[i+1]-t[i]
    else:
        Sum += T
        
print(Sum)