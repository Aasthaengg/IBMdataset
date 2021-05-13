n = int(input())
al = list(map(int, input().split()))

buy = 201
ans = 1000
for i in range(n):
    if al[i] < buy:
        buy = al[i]

    elif al[i] > buy:
        ans = ans//buy*al[i] + ans%buy
        buy = al[i]
    # print(al[i], buy, ans)

print(int(ans))