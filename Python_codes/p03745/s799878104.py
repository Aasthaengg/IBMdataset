N = int(input())
A = list(map(int, input().split()))

cnt = 0
flag = 0

for i in range(N-1):
  if A[i+1]-A[i] > 0:
    if flag == 1:
      cnt +=0
    elif flag == -1:
      cnt +=1
      flag = 0
    elif flag ==0:
      flag = 1
  elif A[i+1]-A[i] < 0:
    if flag == 1:
      cnt +=1
      flag =0
    elif flag ==-1:
      cnt +=0
    elif flag ==0:
      flag = -1
  elif A[i+1]-A[i] == 0:
    flag += 0
      
    
print(cnt+1)