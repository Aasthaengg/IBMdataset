input()
(*a,) = map(int, input().split())

ただの倍数 = 1
for i in set(a):
    ただの倍数 *= i
ans = ただの倍数 / sum(ただの倍数 // i for i in a)
print([ans, int(ans)][ans % 1 == 0])