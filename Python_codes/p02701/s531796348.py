c={}
N=int(input())
for i in range(N):
  s=input()
  if s not in c:
    c[s]=0
print(len(c))