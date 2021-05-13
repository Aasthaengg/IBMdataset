
n = int(input())
a = [int(i) for i in input().split()]

ans = 0
for i in range(len(a)):
  ans += a[i]

print(ans - n)