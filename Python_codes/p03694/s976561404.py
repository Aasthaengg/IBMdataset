n = int(input())
mina = 1000
maxa = 0
A = list(map(int,input().split()))
for i in range(n):
  mina = min(mina,A[i])
  maxa = max(maxa,A[i])
print(maxa - mina)  