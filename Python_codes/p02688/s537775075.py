n,k = map(int,input().split())
people = list(range(1,n+1))

li = []
for i in range(k) :
  gomi = input()
  [li.append(int(j)) for j in input().split()]
st = set(li)
  
ans = 0
for i in people :
  if not i in st :
    ans += 1
print(ans)