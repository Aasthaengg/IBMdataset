n, *a = map(int, open(0).read().split())

set_a = set(a)
set_a = sorted(set_a)

ans = 'No'

if len(set_a) == 1 and a[0] == 0:
    ans = 'Yes'

if len(set_a) == 2 and n%3 == 0 and a.count(0) == n//3 and a.count(set_a[1]) == 2*n//3:
    ans = 'Yes'

if len(set_a) == 3 and n%3 == 0:
    if set_a[0] ^ set_a[1] ^ set_a[2] == 0:
        ans = 'Yes'
        for i in range(3):
            if a.count(set_a[i]) != n//3:
                ans = 'No'
                break
print(ans)