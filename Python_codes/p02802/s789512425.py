N,M = map(int,input().split())

AC = [0 for i in range(N+1)]
WA = [0 for i in range(N+1)]

for i in range(M):
    a,b=input().split()
    a2 = int(a)
    if b == 'AC':
      AC[a2 - 1] = 1
    elif b == 'WA' and AC[a2 - 1] == 0:
      WA[a2-1]+= 1

ans_WA = 0
for i, j in zip(WA, AC):
  ans_WA += i * j
  
print(sum(AC), ans_WA)