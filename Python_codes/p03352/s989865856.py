x = int(input())

ans = 0
if x == 1:
    ans = 1
else:
    for i in range(2, int(x**0.5)+1):
        j = 2
        while True:
            if i**j > x:
                break
            else:
                ans = max(i**j, ans)
                j += 1

print(ans)
