n=int(input())
n=3**n
a=list(map(int,input().split()))

a=[2 if i%2==0 else 1 for i in a]

cnt=1

for i in a:
  cnt*=i
  
  
print(n-cnt)