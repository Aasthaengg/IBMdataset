n = int(input())
v = list(map(int, input().split()))

if len(set(v)) == 1:
    print(n // 2)
else:
    cnt_even = [[0, i] for i in range(10 ** 5 + 1)]
    cnt_odd = [[0, i] for i in range(10 ** 5 + 1)]
    for i in range(n):
        if i % 2 == 0:
            cnt_even[v[i]][0] += 1
        else:
            cnt_odd[v[i]][0] += 1

    cnt_even.sort()
    cnt_odd.sort()

    if cnt_even[-1][1] == cnt_odd[-1][1]:
        print(n - max(cnt_even[-1][0] + cnt_odd[-2][0], cnt_even[-2][0] + cnt_odd[-1][0]))
    else:
        print(n - cnt_even[-1][0] - cnt_odd[-1][0])