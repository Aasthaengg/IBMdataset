n=int(input())
a=list(map(int,input().split()))
is_even=[]
c=1
for x in a:
    c*=2 if x%2==0 else 1
print(3**n-c)