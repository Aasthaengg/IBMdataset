n = int(input())
p = [int(z) for z in input().split()]
k = sorted(p)
poss = False

for i in range(n):
      for j in range(i+1,n):
            new = p[:i]+[p[j]]+p[i+1:j]+[p[i]]+p[j+1:]
            #print(new)
            if (new)==k:
                  poss = True
                  break
if (p==k):
      poss=True

if (poss):
      print("YES")
else:
      print("NO")
