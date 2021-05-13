a,b,k = map(int,input().split())
min_ = min(a,b)
divisors = []
for i in range(1,min_+1,1):
    if(a%i == 0 and b%i == 0 ):
        divisors.append(i)
print(sorted(divisors,reverse=True)[k-1])