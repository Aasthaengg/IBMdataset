h, w = map(int, input().split())
n = int(input())
a = list(map(int, input().split()))

c = 0
for i in range(h):
    ans = []
    for j in range(w):
        ans.append(str(c + 1))
        a[c] -= 1
        if a[c] == 0:
            c += 1

    if i % 2 == 0:
        print(' '.join(ans))
    else:
        print(' '.join(ans[::-1]))
