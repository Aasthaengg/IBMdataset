A = input()

dp = [0]*len(A)
dp[0] = 1
dic = {chr(ord('a')+i):0 for i in range(26)}
dic[A[0]] += 1

for i in range(1,len(A)):
  dp[i] = dp[i-1] + i - dic[A[i]]
  dic[A[i]] += 1
  
print(dp[-1])