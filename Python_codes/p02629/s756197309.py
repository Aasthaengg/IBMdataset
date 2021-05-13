n=int(input())
alf = list("abcdefghijklmnopqrstuvwxyz")
ans=""
i=0
while n-26**i>=0:
  n-=26**i
  i+=1

for j in range(i):
  n,b=divmod(n,26)
  ans+=str(alf[b])
print(ans[::-1])