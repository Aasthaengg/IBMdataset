N, A, B, C, D = map(int, input().split())
S = str(input())

Sarr = [True if s == '.' else False for s in S]
#print(Sarr)

def canmove(st):
  global N, Sarr
  can = [False] * N
  can[st-1] = True
  for i in range(st, N):
    if Sarr[i]:
      if can[i-1] or can[i-2]:
        can[i] = True
  return can

Acan = canmove(A)
Bcan = canmove(B)
#print(Acan)
#print(Bcan)

ans = Acan[C-1] and Bcan[D-1]
#print(ans)

def canpass(st, ed):
  global Sarr
  for i in range(st, ed-1):
    if Sarr[i] and Sarr[i+1] and Sarr[i+2]:
      return True
  return False

if C > D:
  ans = ans and canpass(B-2, D)
#print(ans)

if ans:
  print('Yes')
else:
  print('No')