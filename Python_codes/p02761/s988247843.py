n,m=map(int, input().split())
sl=[]
sc=["0"]*(n+1)
for _ in range(m):
  s,c = map(int, input().split())
  if s == 1 and c == 0 and n != 1:
    print(-1)
    exit()
  if s in sl and sc[s] != c:
    print(-1)
    exit()
  sl.append(s)
  sc[s]=c
  
if n >= 2 and sc[1] == "0":
  sc[1]=1
#print(sc)
print(int(''.join(map(str, sc[1:n+1]))))