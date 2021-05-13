N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)

now = A[0]
tateyoko = [0, 0]
count = 0
nowflag = False
for i in range(1, N):
  if (A[i] == now) and (not nowflag):
    tateyoko[count] = now
    count += 1
    nowflag = True
  else:
    nowflag = False
  if count == 2:
    break
  now = A[i]
  
print(tateyoko[0] * tateyoko[1])
