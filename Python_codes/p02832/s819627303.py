N = int(input())
A = tuple(map(int, input().split(' ')))

i = 1
n = 0
for a in A:
    if a == i:
        i += 1
    else:
        n += 1

if n >= N:
    print(-1)
else:
    print(n)
