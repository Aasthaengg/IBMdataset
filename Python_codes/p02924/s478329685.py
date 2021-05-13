n = int(input())

ans = n * (n // 2)
if (n - 1) % 2 == 0:
   print(ans)
else:
   print(ans - int(n / 2))
