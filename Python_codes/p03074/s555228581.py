N, K = map(int, input().split())
S = input()

lst = []
b = S[0]
if b == '0':
  lst.append(0)
  
cnt = 1
for i in range(1, len(S)):
  if b != S[i]:
    lst.append(cnt)
    cnt = 1
  else:
    cnt += 1
  b = S[i]
lst.append(cnt)

if b == '0':
  lst.append(0)

l = len(lst)
if K >= l//2:
  print(N)
else:
  tmp = sum(lst[:2*K+1])
  rlt = tmp
  for i in range(2,l-2*K,2):
    tmp += lst[2*K+i-1] + lst[2*K+i] - lst[i-1] - lst[i-2]
    rlt = max(rlt, tmp)
  print(rlt)