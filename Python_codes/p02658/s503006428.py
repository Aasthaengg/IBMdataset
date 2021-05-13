n = int(input())
a = [int(x) for x in input().split()]
a.sort()

def check():
  ans = 1
  for i in range(n):
    ans *= a[i]
    if ans == 0:
      return 0
    if ans > 10 ** 18:
      return -1
  return ans
p = check()
print(p)