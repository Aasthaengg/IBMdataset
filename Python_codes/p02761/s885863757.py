def solve():
    N,M = [int(i) for i in input().split()]
    digits = ['0'] * N
    digits[0] = '0' if N == 1 else '1'
    targets = set([])
    for i in range(M):
        s,c = [int(num) for num in input().split()]
        target = s - 1
        if target == 0 and c == 0 and N != 1:
            digits = ['-1']
            break
        if target in targets and str(c) != digits[target]:
            digits = ['-1']
            break
        else:
            digits[s-1] = str(c)
            targets.add(s-1)
    print(''.join(digits))

if __name__ == "__main__":
    solve()