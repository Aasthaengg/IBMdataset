import sys
def input(): return sys.stdin.readline().strip()

def main():
    H, W = map(int, input().split())
    S = ['.' * W] + [input() for _ in range(H)] + ['.' * W]
    if W == 1:
        for i in range(1, H + 1):
            if S[i] == '#':
                print('#')
                continue
            string = S[i - 1] + S[i + 1]
            cnt = string.count('#')
            print(str(cnt))
        return
    for i in range(1, H + 1):
        code = ""
        for j in range(W):
            if S[i][j] == '#':
                code += '#'
                continue
            if j == 0:
                string = S[i - 1][:2] + S[i][1] + S[i + 1][:2]
                cnt = string.count('#')
                code += str(cnt)
                continue
            if j == W - 1:
                string = S[i - 1][-2:] + S[i][-2] + S[i + 1][-2:]
                cnt = string.count('#')
                code += str(cnt)
                continue
            string = S[i - 1][j - 1:j + 2] + S[i][j - 1] + S[i][j + 1] + S[i + 1][j - 1:j + 2]
            cnt = string.count('#')
            code += str(cnt)
            continue
        print(code)


if __name__ == "__main__":
    main()
