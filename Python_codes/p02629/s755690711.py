N = int(input())
ans = ''
while N>0:
    N -= 1
    ans = chr(N%26+97) + ans
    N = N // 26
print(ans)

