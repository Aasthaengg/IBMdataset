def resolve():
    N = int(input())
    H = list(map(int, input().split()))
    ans = [0]
    count = 0
    for i in range(len(H) - 1):
        if H[i] >= H[i + 1]:
            count += 1
        else:
            ans.append(count)
            count = 0
    if count != 0:
        ans.append(count)
    print(max(ans))
resolve()