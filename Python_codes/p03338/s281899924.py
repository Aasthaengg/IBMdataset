N = int(input())
s = input()

def countSameChar(x,y):
  cnt = 0
  for char in [chr(ord("a")+i) for i in range(26)]:
    if char in x and char in y:
      cnt += 1
  return cnt

def solve(n,s):
  ans = 0
  for i in range(n-2):
    x = s[:i+1]
    y = s[i+1:]
    ans = max(ans,countSameChar(x,y))
  return ans

print(solve(N,s))