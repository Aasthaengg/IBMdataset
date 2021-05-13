n = int(input())
la = list(input().split())

if n % 2 == 0:
    l = list(reversed(la))[::2]
    l = l + la[::2]
    print(" ".join(l))

else:
    l = list(reversed(la))[::2]
    l = l + la[1::2]
    print(" ".join(l))