n = int(input())
a = tuple(map(int,input().split()))

ans = 0
for a_i in a:
  while a_i%2==0:
    ans+=1
    a_i//=2
print(ans)