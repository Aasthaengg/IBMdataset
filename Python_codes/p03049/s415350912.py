N=int(input())
s = [input() for _ in range(N)]
t = sum([s[i].count("AB") for i in range(N)])

p = sum([1 if s[i][-1] == "A" else 0 for i in range(N)])
q = sum([1 if s[i][0] == "B" else 0 for i in range(N)])
r = sum([1 if s[i][0] == "B" and s[i][-1] == "A" else 0 for i in range(N)])

p -= r
q -= r

ans=t
#print(t)
#print(p,q,r)

if r==0:
  ans += min(p,q)
else:
  ans += r-1
  if p>=1:
    p = p-1
    ans +=1
  if q>=1:
    q = q-1
    ans +=1
  ans += min(p,q)
print(ans)