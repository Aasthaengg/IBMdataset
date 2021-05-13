h, w, k = map(int, input().split())
S = [list(input()) for _ in range(h)]
ans = []
piece_num = 1
cnt = 0
for i in range(h):
    if "#" in S[i]:
        ans = []
        for j in range(w):
            if S[i][j] == "#":
                stroke = j + 1 - len(ans)
                for _ in range(stroke):
                    ans.append(str(piece_num))
                piece_num += 1
        if len(ans) < w:
            x = ans[-1]
            stroke = w - len(ans)
            for _ in range(stroke):
                ans.append(x)
    if ans:
        pre_loop = i - cnt
        for _ in range(pre_loop):
            print(*ans)
            cnt += 1

        print(*ans)
        cnt += 1
