n, m = map(int, input().split())

ans = 0


if n >= 3 and m >= 3:
    ans = (n-2) * (m-2)
    print(ans)

elif (n == 2 and m >= 3) or (m == 2 and n >= 3):
    ans = 0
    print(ans)

elif (n == 1 and m >= 3) or (m == 1 and n >= 3):
    ans = n * m - 2
    print(ans)

elif n == 2 and m == 2:
    ans = 0
    print(ans)
    
elif n == 1 and m == 1:
    ans = 1
    print(ans)
    
else:
    ans = 0
    print(ans)
