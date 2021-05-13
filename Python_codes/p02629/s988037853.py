N = int(input())
ans = ''

for i in range(1,99):
    if 26**i >= N:
        N -= 1
        for s in range(i):
            ans += chr(ord('a') + N%26)
            N //= 26
        break
    else:
        N -= 26**i

print(ans[::-1])
