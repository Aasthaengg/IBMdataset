n = int(input())
a = list(map(int, input().split()))

ai = max(a)
a.sort(key=lambda x: abs(ai//2 - x))
aj = a[0]
for i in a:
    if ai==i: continue
    else:
        aj = i
        break

print('{} {}'.format(ai, aj))