N = int(input())

ans = 2 * 10**5

for n in range(1,N//2 + 1):
  a = n
  b = N - n
  
  sum_a = sum(list(map(int,list(str(a)))))
  sum_b = sum(list(map(int,list(str(b)))))
  
  ans = min(ans,sum_a+sum_b)
print(ans)