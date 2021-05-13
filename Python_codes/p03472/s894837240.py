N, H = map(int, input().split())
A = list()
B = list()
for i in range(N):
  a, b = map(int, input().split())
  A.append(a)
  B.append(b)
A.sort(reverse = True)
B.sort(reverse = True)
cnt = 0
b = 0
while(H > 0 and b<=N-1 and cnt==b):
  cnt += 1
  if(B[b]>A[0]):
    H -= B[b]
    b += 1
if(H <= 0):
  print(b)
else:
  print(b +(H-1)//A[0]+1)