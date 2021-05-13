N,A,B=map(int,input().split())

def sum_keta(n):
    sum=0
    while n>0:
        sum+=n%10
        n=n//10
    return sum

total=0
for n in range(1,N+1):
    if A<=sum_keta(n)<=B:
        total+=n
    else:
        continue

print(total)