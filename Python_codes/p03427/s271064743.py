N = int(input())
topdigi = int(str(N)[0])
keta = len(str(N))

candidate = int(str(topdigi) + "9" * (keta - 1))

if candidate > N:
    ans = (topdigi - 1) + 9 * (keta - 1)
else:
    ans = topdigi + 9 * (keta - 1)
print(ans)
