H, W, A, B = map(int, input().split())
ans = []
for h in range(H):
    tmp = ""
    for w in range(W):
        if h < B:
            if w < A:
                tmp += "0"
            else:
                tmp += "1"
        else:
            if w < A:
                tmp += "1"
            else:
                tmp += "0"
    ans.append(tmp)
print("\n".join(ans))
