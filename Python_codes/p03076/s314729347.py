A = [int(input()) for i in range(5)]
num = 10
ans = 0
for i in range(5):
  num = min((A[i]-1)%10,num)
  ans += -(-A[i]//10*10)
print(ans + num - 9)