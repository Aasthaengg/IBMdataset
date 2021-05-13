n=int(input())
sum=0
for i in range(n):
    a,b = list(map(int,input().split()))
    sum+=b-a+1
print(sum)
