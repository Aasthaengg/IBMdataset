# 解説AC
N,K,C = map(int, input().split())
S = [""] + list(input())

# cnt1[i]: [1,i]での最大労働可能日数
cnt1 = [0] * (N + 2)
cnt, can = 0, 0
for i in range(1, len(S)):
    if S[i] == "o" and i >= can:
        cnt += 1
        can = i + (C + 1)
    cnt1[i] = cnt

# cnt2[i]: [i,N]での最大労働可能日数
cnt2 = [0] * (N + 2)
cnt, can = 0, N
for i in range(len(S) - 1, 0, -1):
    if S[i] == "o" and i <= can:
        cnt += 1
        can = i - (C + 1)
    cnt2[i] = cnt

ans = []
for i, s in enumerate(S[1:], 1):
    if s == "x": continue
    # i日目に働かないと、条件を満たさない場合
    if cnt1[i - 1] + cnt2[i + 1] < K:
        ans.append(i)

print(*ans, sep="\n")