S = input()

ans = [0 for _ in range(len(S))]
r = 0
l = 0
tmp = 0
for i in range(len(S)):
    if(S[i] == "R"):
        if(l > 0):
            ans[tmp] = r//2+l-l//2
            ans[tmp-1] = r-r//2+l//2
            r = 0
            l = 0
        r += 1
    else:
        if(S[i-1] == "R"):
            tmp = i
        l += 1
        if(i == len(S)-1):
            ans[tmp] = r//2+l-l//2
            ans[tmp-1] = r-r//2+l//2
print(*ans)