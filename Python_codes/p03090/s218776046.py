import sys

def solve():
    input = sys.stdin.readline
    N = int(input())
    Ans = []
    AnsNum = 0
    if N % 2 == 0:
        for i in range(1, N):
            for j in range(i + 1, N + 1):
                if i + j != N + 1:
                    Ans.append((i, j))
                    AnsNum += 1
    else:
        for i in range(1, N):
            for j in range(i + 1, N + 1):
                if i + j != N:
                    Ans.append((i, j))
                    AnsNum += 1
    print(AnsNum)
    for i in range(AnsNum):
        print(" ".join(map(str, Ans[i])))


    return 0

if __name__ == "__main__":
    solve()