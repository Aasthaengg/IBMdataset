N = int(input())
ans = []
while N:
    N -= 1
    a = N % 26
    ans.append(chr(ord('a') + a))
    N //= 26
ans.reverse()
print(''.join(ans))