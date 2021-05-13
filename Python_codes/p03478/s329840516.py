N,A,B=map(int,input().split(' '))
answer = 0
for i in range(N):
  n = sum(int(j) for j in str(i+1))
  if n >= A and n <= B:
    answer += i+1
print(answer)