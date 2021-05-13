

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    H, W = read_ints()
    A = []
    for _ in range(H):
        A.append(read_ints())
    answer = []
    last = None
    for i in range(H):
        for j in range(W):
            if i%2 == 1:
                j = W-j-1
            if last is not None and A[last[0]][last[1]]%2 == 1:
                A[i][j] += 1
                answer.append((last[0]+1, last[1]+1, i+1, j+1))
            last = (i, j)
    print(len(answer))
    for a in answer:
        print(*a)


if __name__ == '__main__':
    solve()
