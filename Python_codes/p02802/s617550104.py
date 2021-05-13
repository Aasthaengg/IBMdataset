def solve():
    N, M = [int(i) for i in input().split()]
    ans = set()
    pen = 0
    arr = [0] * N
    for _ in range(M):
        p, s = input().split()
        if s == 'AC' and int(p) not in ans:
            ans.add(int(p))
            pen += arr[int(p) - 1]
        if s == 'WA':
            arr[int(p) - 1] += 1
    print(f'{len(ans)} {pen}')

if __name__ == "__main__":
    solve()