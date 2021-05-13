N,C,K = list(map(int,input().split()))
T = []
for i in range(N):
    T.append(int(input()))
T.sort()
cnt = 0

Bus = 1
Capa = 0
first = T[0]
for i in range(N):
    t = T[i]
    if t-first>K or Capa+1>C:
        Bus+=1
        Capa = 1
        first = t
    else:
        Capa += 1
print(Bus)