N = int(input())
ans = ''
i = 1

while N > 0:
    N -= 1
    ans = chr(ord('a') + N % 26) + ans

    N = N // 26

print(ans)
exit()
