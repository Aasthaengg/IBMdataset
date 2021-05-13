a,b,c=map(int,input().split())
k=int(input())
lis=[]
for i in range(0,k+1):
  for j in range(0,k-i+1):
      atai=a*(2**i)+b*(2**j)+c*(2**(k-i-j))
      if not atai in lis:
        lis.append(atai)
lis.sort()
print(lis[-1])