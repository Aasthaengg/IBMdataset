a1,b1 = map(int,input().split())
a2,b2 = map(int,input().split())
a3,b3 = map(int,input().split())

ls = [a1,b1,a2,b2,a3,b3]

ans = "YES"
for i in range(1,5,1):
  if ls.count(i) == 3:
    ans ="NO"
print(ans)