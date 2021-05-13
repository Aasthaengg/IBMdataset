N = int(input())
c = []
while N > 0:
    N -= 1
    c.append(N % 26)
    N //= 26
c.reverse()
ans = "".join(chr(ord("a") + x) for x in c)
print(ans)