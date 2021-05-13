n=int(input())
A=list(map(int,input().split()))
m=3**n
b=1
for a in A:
    if a%2==0:
        b*=2
print(m-b)