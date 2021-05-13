data = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#print(ord("A"))
#print(ord("Z")-65)

n=int(input())
a=input()
ans=""
for i in a:
  p = (ord(i)-65+n)%26
  ans+=data[p]
print(ans)