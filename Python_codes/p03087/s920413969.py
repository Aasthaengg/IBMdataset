N,Q = map(int,input().split())
S = input()
lr = [list(map(int,input().split())) for _ in range(Q)]
wa = [0,0]
num = 0
for i in range(2,N+1):
  if S[i-2:i] == "AC":
    num += 1
  wa.append(num)
left = 0
right = 0
for i in range(Q):
  left = lr[i][0]
  right = lr[i][1]
  print(wa[right]-wa[left])