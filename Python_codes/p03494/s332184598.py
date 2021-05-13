#3
#8 12 40
n=int(input())
ai=list(map(int,input().split()))
b=[]
for a in ai:
  count =0
  while a%2==0 :
    count+=1
    a/=2
  b.append(count)
print(min(b))