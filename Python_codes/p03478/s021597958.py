#n=int(input())
n,a,b=map(int,input().split())
#l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]

def sum_of_digit(n):
    res=0
    while n>0:
        res+=n%10
        n=n//10
    return res
count=0
for i in range(1,n+1):
    if a<= sum_of_digit(i) and sum_of_digit(i) <=b :
        count+=i
print(count)
