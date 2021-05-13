N, K = map(int, input().split())
S = input()
cnt = 1
counts = []

if S[0]=='0':
  counts.append(0)
if N == 1:
  counts.append(1)
  
for i in range(1,N):
  if S[i-1]!=S[i]:
    counts.append(cnt)
    cnt = 1
  else:
    cnt += 1
  #print(i)
  if i == N-1:
    counts.append(cnt)

#print(counts)
K = min(K,len(counts)//2)
for i in range(len(counts)//2-K+1):
  if i == 0:
    s = sum(counts[:2*K+1])
    m = s
  else:
    s += sum(counts[2*(i+K)-1:2*(i+K)+1])-sum(counts[2*i-2:2*i])
    m = max(m,s)
  #print(s)
print(m)
