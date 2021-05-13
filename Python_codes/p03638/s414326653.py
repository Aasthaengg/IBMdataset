import sys

input = sys.stdin.readline


def main():
    H, W = [int(x) for x in input().split()]
    N = int(input())
    A = [int(x) for x in input().split()]

    ans = [[0] * W for j in range(H)]

    c = 0
    for j in range(H):
        if j % 2 == 0:
            for i in range(W):
                if A[c] == 0:
                    c += 1
                A[c] -= 1
                ans[j][i] = c + 1
        else:
            for i in range(W - 1, -1, -1):
                if A[c] == 0:
                    c += 1
                A[c] -= 1
                ans[j][i] = c + 1

    for a in ans:
        print(*a)


    
    
    

if __name__ == '__main__':
    main()

