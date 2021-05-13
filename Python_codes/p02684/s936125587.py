def main():

    n, k = (int(i) for i in input().split())
    tel = [int(i) - 1 for i in input().split()]

    # take one step with our 'slo' walker
    slo = tel[0]
    fas = tel[slo]
    k -= 1

    while k != 0 and slo != fas:
        slo = tel[slo]
        fas = tel[tel[fas]]
        k -= 1

    if k == 0:
        print(slo + 1)
        return

    cyc = 0
    while k != 0:
        slo = tel[slo]
        cyc += 1
        k -= 1
        if fas == slo:
            break

    k = k % cyc

    for i in range(k):
        slo = tel[slo]

    print(slo + 1)


main()
