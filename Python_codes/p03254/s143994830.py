import itertools

N, x = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
a = list(itertools.accumulate(a))

cnt = 0

for i in range(len(a)):
    if x > a[i]:
        if i == len(a)-1:
            break
        cnt += 1
    elif x == a[i]:
        cnt += 1
        break
    else:
        break

print(cnt)