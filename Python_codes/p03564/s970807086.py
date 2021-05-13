N = int(input())
K = int(input())
 
def func(a):
  ans = 1
  for n in range(a):
    ans = ans*2
  for n in range(N-a):
    ans = ans + K
  return ans
 
print(min([func(i) for i in range(N+1)]))