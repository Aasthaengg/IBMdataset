N=int(input())
s,t=[],[]
for _ in range(N):
  a,b=input().split()
  s.append(a)
  t.append(int(b))
X=input()
print(sum(t[(s.index(X)+1):]))
