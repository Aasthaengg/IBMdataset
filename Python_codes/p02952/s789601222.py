n = input()

digit = len(n) 
ans = 0

for i in range(1, digit//2 + 1):
  ans += 10**(2*i-1) - 10**(2*i-2)

if len(n) % 2 == 1:
  nn = int(n)
  ans += nn - 10**(len(n)-1) + 1

print(ans)