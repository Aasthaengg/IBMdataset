N=int(input())
li = []
ti = []
for i in range(N):
  l,t = input().split()
  li.append(l)
  ti.append(int(t))
S=input()
print(sum(ti[li.index(S)+1:]))