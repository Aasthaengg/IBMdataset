n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ll = [[i - j, i, j] for i, j in zip(a, b)]

ll.sort(reverse=True)
start = n -1

if sum(a) < sum(b):
    print(-1)
    exit(0)

for i in range(n):
    while ll[i][0] > 0:
        if ll[start][0] < 0:
            if ll[i][0] + ll[start][0] >= 0:
                ll[i][0] += ll[start][0]
                ll[start][0] = 0
                start -= 1
            elif ll[i][0] + ll[start][0] < 0:
                ll[start][0] += ll[i][0]
                ll[i][0] = 0
                break
        else:
            break

cnt = 0

for l in ll:
    if l[1] - l[2] != l[0]:
        cnt += 1

print(cnt)
"""
方針
- b - aが小さい要素を使って、b - aが大きい要素を埋めていく
- 

"""
