import sys
input = sys.stdin.readline

def main():
  n, k = map(int, input().split())
  a_list = list(map(int, input().split()))
  dp = [False]*(k+1)

  for i in range(1,k+1):
    for j in range(n):
      if i-a_list[j] >= 0:
        dp[i] |= not(dp[i-a_list[j]])


  if dp[k]:
    print('First')
  else:
    print('Second')
main()