N = int(input())
a = list(map(int, input().split()))
max_a = max(a)
if max_a == 0:
    print('Yes')
    exit()

if N % 3 != 0:
    print('No')
    exit()

if a.count(max_a) == 2 * N // 3 and a.count(0) == N // 3:
    print('Yes')
    exit()

set_a = list(set(a))
if len(set_a) == 3 and set_a[0] ^ set_a[1] ^ set_a[2] == 0:
    if a.count(set_a[0]) == a.count(set_a[1]) == a.count(set_a[2]):
        print('Yes')
        exit()

print('No')
