N = int(input())

i = 1
T = 26
ans = ""
while True:
    if N <= T ** i:
        N -= 1
        while i > 0:
            N, r = divmod(N, T)
            ans += chr(r + ord('a'))
            i -= 1
        break
    else:
        N -= T ** i
        i += 1
print(ans[::-1])
