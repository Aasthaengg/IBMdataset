n,k = map(int,input().split())
count = 0
for i in range(k,n+2):
    count = (count+i*(n-i+1)+1)%(1e+9+7)
print(int(count))