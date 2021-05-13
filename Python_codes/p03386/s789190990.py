a, b, k = map(int, input().split())

l = [i for i in range(a, b+1) if (i < a+k) or (i > b-k)]

print(*l, sep="\n", end="")