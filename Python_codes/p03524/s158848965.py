s=list(input())
an=s.count("a")
bn=s.count("b")
cn=s.count("c")
cl=[an, bn, cn]
m=max(cl)
cl.remove(m)
for n in cl:
  if (m-1)!=n and (m-1)!=n-1:
    print("NO")
    exit()
print("YES")
