N = int(input())
S = list(input())

bl = [0] * (N+1)    # 左に黒が何個あるか
wr = [0] * (N+1)    # 右に白が何個あるか
for i in range(N): bl[i+1] = bl[i] + (1 if S[i] == '#' else 0)
for i in range(N-1,-1,-1): wr[i] = wr[i+1] + (1 if S[i] == '.' else 0)

ans = N+1
for i in range(N+1): ans = min(ans, bl[i]+wr[i])
print(ans)