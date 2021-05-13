def solve():
    ret = 0
    most_right = 0
    for left, right in sects:
        if left < most_right:
            continue
        ret += 1
        most_right = right
    print(ret)

if __name__ == "__main__":
    N, M = map(int, input().split())
    sects = []
    for _ in range(M):
        sects.append(list(map(int, input().split())))
    sects.sort(key=lambda x: x[1])
    solve()