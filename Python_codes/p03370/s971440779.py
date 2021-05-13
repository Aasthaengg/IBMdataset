N, X = map(int, input().split())
marr= []

for i in range(0,N):
  m = int(input())
  marr.append(m)

marr=sorted(marr)
print(len(marr)+((X-sum(marr))//marr[0]))