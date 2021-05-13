n=int(input())
i=list(map(int,input().split()))
i.sort()
temp=1
size=i[0]
for k in range(1,n):
  if size*2>=i[k]:
    temp+=1
    size+=i[k]
  else:
    temp=1
    size+=i[k]
print(temp)
