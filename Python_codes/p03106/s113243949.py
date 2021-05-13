a,b,k=map(int,input().split())
war=[]
for i in range(1,max(a,b)+1):
  if a%i==0 and b%i==0:
    war.append(i)
war.reverse()

print(war[k-1])