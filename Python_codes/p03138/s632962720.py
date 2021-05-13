def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    l = []
    for _ in range(40):
        cnt = 0
        for i in range(n):
            if a[i] & 1:
                cnt += 1
            a[i] >>= 1
        l.append(cnt)

    pows = [1]
    for _ in range(39):
        pows.append(pows[-1] * 2)

    if k == 0:
        print(sum([l[i] * pows[i] for i in range(40)]))
        exit()

    # when it does not use the biggest bit of k
    ans1 = 0
    for i in range(k.bit_length() - 1):
        if l[i] < n - l[i]:
            ans1 += (n - l[i]) * pows[i]
        else:
            ans1 += l[i] * pows[i]
    for i in range(k.bit_length() - 1, 40):
        ans1 += l[i] * pows[i]

    # when it use the biggest bit of k
    ans2 = 0
    ans3 = 0
    for i in range(40):
        if l[i] < n - l[i]:
            if k & 1:
                ans2 += (n - l[i]) * pows[i]
            else:
                ans2 += l[i] * pows[i]
            ans3 += (n - l[i]) * pows[i]
        else:
            if k & 1:
                ans2 = ans3 + l[i] * pows[i]
            else:
                ans2 += l[i] * pows[i]
            ans3 += l[i] * pows[i]
        k >>= 1

    print(max(ans1, ans2))

main()