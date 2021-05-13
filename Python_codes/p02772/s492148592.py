n=int(input())
l=list(map(int,input().split()))
flag=True
li=[]
for i in range(len(l)):
  if l[i]%2==0:
    li.append(l[i])
for i in range(len(li)):
  if li[i]%3!=0 and li[i]%5!=0:
    flag=False
#print(li)
if flag==True:
  print("APPROVED")
else:
  print("DENIED") 