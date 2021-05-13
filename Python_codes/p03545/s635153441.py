N = list(map(int, list(input())))
for i in range(2 ** 3):
    total = N[0]
    ans = []
    for j in range(3):
        if i >> j & 1:
            total += N[j + 1]
            ans.append('+')
        else:
            total -= N[j + 1]
            ans.append('-')
    if total == 7:
        joy = ''
        for i in range(3):
            joy += str(N[i])
            joy += str(ans[i])
        joy += str(N[-1])
        joy += '=7'
        print(joy)
        break
