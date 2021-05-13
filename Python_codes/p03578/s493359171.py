from collections import Counter

N=int(input())
D=list(map(int, input().split()))
M=int(input())
T=list(map(int, input().split()))

dd=Counter(D)
td=Counter(T)

ddl=list(dd.items())
tdl=list(td.items())

for k, v in tdl:
  if dd[k]<v:
    print("NO")
    exit()

print("YES")