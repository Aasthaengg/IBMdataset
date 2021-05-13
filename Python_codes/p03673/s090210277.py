n = int(input())
a = list(map(int, input().split()))
if n % 2 == 0:
  l_1 = [a[n-1-2*i] for i in range(n//2)]
  l_2 = [a[2*i] for i in range(n//2)]
else:
  l_1 = [a[n-1-2*i] for i in range((n+1)//2)]
  l_2 = [a[2*i+1] for i in range(n//2)]
print(*l_1, *l_2)