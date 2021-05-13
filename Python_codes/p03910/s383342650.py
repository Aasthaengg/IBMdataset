n=int(input())
ans=[1]
i=2

while n>sum(ans):
  ans.append(i)
  i+=1
if n!=sum(ans):
  ans.remove(sum(ans)-n)
[print(i) for i in ans]