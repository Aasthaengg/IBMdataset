N = int(input())
A = list(map(int,input().split()))
for i in range(N):
  A[i] -= i+1
#print(A)
A.sort()
dic = {}
for x in A:
  if x not in dic:
    dic[x] = 1
  else:
    dic[x] += 1
S = list(dic.keys())
now = 0
for x in A:
  now += abs(A[0]-x)
#print(now)
prev = A[0]
left = dic[S[0]]; right = N- left
for i in range(1,len(S)):
  dif = (left-right)*(S[i]-S[i-1])
  if dif < 0:
    now += dif
  left += dic[S[i]]
  right -= dic[S[i]]
print(now)