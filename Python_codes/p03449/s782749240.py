N = int(input())
A1 =list(map(int, input().split()))
A2 =list(map(int, input().split()))
 
candy = []
 
def sum_A1(x):
  cnt = 0
  for i in range(x+1):
    cnt += A1[i]
  return cnt
 
def sum_A2(x):
  cnt = 0
  for i in range(x,N):
    cnt += A2[i]
  return cnt
 
for i in range(N):
  candy.append(sum_A1(i) + sum_A2(i))
  
print(max(candy))