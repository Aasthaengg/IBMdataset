n = int(input())

a = list(map(int, input().split(' ')))
b = list(map(int, input().split(' ')))

c = 0
for i in range(n):
    ai = a[i]
    bi = b[i]
    if ai < bi:
        c += (bi-ai)//2
    else:
        c -= (ai-bi)
print('Yes' if c >= 0 else 'No')
