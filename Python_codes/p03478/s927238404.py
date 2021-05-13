#N = int(input())
#S = str(input())
N, A, B = map(int, input().split())
#C = list(map(int, input().split()))

def su(n):
  n = str(n)
  aa = 0
  for i in range(len(n)):
    aa += int(n[i])
  return aa
  

ans = 0
for i in range(1, N + 1):
  now = su(i)
  if A <= now <= B:
    ans += i
print(ans)
  
  
