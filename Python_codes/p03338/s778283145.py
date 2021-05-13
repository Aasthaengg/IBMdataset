N = int(input())
S = input()
ans = 0
for i in range(1,N):
    cnt = 0
    A,B = set(S[:i]),set(S[i:])
    for j in A:
        if j in B:
            cnt += 1
    ans = max(ans,cnt)
print(ans)