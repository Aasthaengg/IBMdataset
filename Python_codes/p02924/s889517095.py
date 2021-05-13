N = int(input())

if (N -1) % 2 == 0:
  ans = N*(N-1)//2
else:
  ans = N*(N-2)//2 + N//2
  
print(ans)