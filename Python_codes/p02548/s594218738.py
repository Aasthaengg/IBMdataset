N = int(input())
 
ans = 0
for a in range(1, N ):
   for b in range(1, N // a + 1):
      if a * b < N:
         ans += 1
 
print(ans)