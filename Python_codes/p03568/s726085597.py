n = int(input())
a = [int(_) for _ in input().split()]

ans = 3**n

if a[0] % 2 == 0:
    cnt = 2
else:
    cnt = 1
for i in range(1, n):
    if a[i] % 2 == 0:
        cnt *= 2
    else:
        pass

print(ans-cnt)
