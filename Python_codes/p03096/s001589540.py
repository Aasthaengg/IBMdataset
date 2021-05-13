import numpy as np

def main():
  mod = 10 ** 9 + 7

  n = int(input())
  nums = [-1]
  for _ in range(n):
      tmp = int(input())
      if nums[-1] != tmp:
          nums.append(tmp)
  #print(nums)

  m = len(nums)

  dp = [1 for _ in range(m)] # i番目の石までは操作を行い、i+1番目以降の石は操作をしない時の場合の数
  colors = [0 for _ in range(max(nums) + 1)] #その時各色が何個、i番目以前にあるのか

  for i in range(1, m):
    dp[i] = (dp[i - 1] + colors[nums[i]]) % mod #i番目の石を利用可能にすることで作れる数列の数は、i - 1番目まででできるものに、i番め以前の数列を利用したもの？
    colors[nums[i]] = dp[i]
    #print(dp, colors)


  print(dp[-1])
  

if __name__ == '__main__':
  main()
