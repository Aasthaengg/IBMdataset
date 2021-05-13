n = int(input())
a = [int(input()) for _ in range(n)]

if a[0] != 0:
    print(-1)
    exit()

l = [-1]
for i in a:
    if i == l[-1] + 1:
        l[-1] += 1
    elif i <= l[-1]:
        l.append(i)
    else:
        print(-1)
        exit()

print(sum(l))
