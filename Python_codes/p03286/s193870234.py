N = int(input())
ans = ""
b = -2
while N:
    n = N % b
    if n:
        ans = "".join(["1", ans])
    else:
        ans = "".join(["0", ans])

    N += n
    b *= - 2
print(ans if ans else 0)

