N = int(input())
ls = []
while N > 0:
    N -= 1
    a = N % 26
    N //= 26
    ls.append(a+97)
print("".join(map(chr, reversed(ls))))
