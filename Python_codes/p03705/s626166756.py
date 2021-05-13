n, a, b = map(int, input().split())

ans = 0
if n >= 2 and a <= b:
    lst_min = a * (n - 1) + b
    lst_max = a + b * (n - 1)
    
    ans = lst_max - lst_min + 1

elif n == 1 and a == b:
    ans = 1

print(ans)