n, *a = map(int, open(0).read().split())

unko = 2
unti = 2
for i in reversed(a):
    unko = unko // i * i + i - 1
    unti = (unti + i - 1) // i * i
if unti >= unko:
    print(-1)
else:
    print(unti, unko)
