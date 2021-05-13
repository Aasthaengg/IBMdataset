s=input()
k=int(input())

li=set()

for p in range(5):
  for i in range(len(s)-p):
    li.add(s[i:i+1+p])
li=list(li)
li.sort()
#print(li)
print(li[k-1])