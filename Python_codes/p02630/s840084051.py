N = int(input())

A_li = list(map(int, input().split()))

Q = int(input())


A_li.sort()
res = sum(A_li)
main_li = {}

now = 0
for i in A_li:
    if i == now:
        main_li[i] += 1
    else:
        main_li[i] = 1
        now = i


# クエリの処理
for _ in range(Q):
    B, C = list(map(int, input().split()))
    if B not in main_li.keys():
        print(res)
        continue
    if C in main_li.keys():
        main_li[C] += main_li[B]
    else:
        main_li[C] = main_li[B]
    res += (C - B) * main_li[B]
    main_li.pop(B)
    print(res)

