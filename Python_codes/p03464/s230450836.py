input()
l=s=2
for i in map(int,input().split()[::-1]):
  s=i*(s//i+[1,0][s%i==0])
  l=i*(l//i+1)-1
print(-1) if s>l else print(s,l)