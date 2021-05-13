def main():
    n = int(input())
    h = [int(i) for i in input().split()]

    d1 = { }
    d2 = { }
    for j in range(n):
        dif = j - h[j]
        tot = j + h[j]
        if dif not in d1:
            d1[dif] = 0
        if tot not in d2:
            d2[tot] = 0

        d1[dif] += 1
        d2[tot] += 1

    npairs = 0
    # print(d1)
    # print(d2)
    for i in range(n):
        dif = i - h[i]
        tot = i + h[i]
        if tot in d1:
            npairs += d1[tot]
        if dif in d2:
            npairs += d2[dif]

    print(npairs // 2)

main()
