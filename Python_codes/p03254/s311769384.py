N, x = map(int, input().split())
a = [int(a) for a in input().split()]

if sum(a) == x:
    print(N)
    exit()

sort_a = sorted(a)
count = 0
for i in range(1,N+1):
    if sum(sort_a[:i]) <= x:
        if i < N:
            count += 1
        else:
            pass
    else:
        break

print(count)