S = input()

ans = 0
for i in range(len(S)):
    for j in range(i+1, len(S)+1):
        for s in S[i:j]:
            if s != "A" and s != "C" and s != "G" and s != "T":
                break
        else:
            ans = max(ans, len(S[i:j]))
print(ans)
