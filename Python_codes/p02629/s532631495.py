n = int(input())
res = []
arufa = []
for i in range(97, 123):
    arufa.append(chr(i))
while n:
    if n == 0:
        break
    n -= 1
    res.append(arufa[int(n % 26)])
    n //= 26
res.reverse()
ans = "".join(res)
print(ans)
