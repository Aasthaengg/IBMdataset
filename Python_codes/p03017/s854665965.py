import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

N, A, B, C, D = lr()
S = input()
# if C > D:
#     if "..." not in S[B-1:D]:
#         print("No")
#         exit(0)
# if "##" in S[A-1:C] or "##" in S[B-1:D]:
#     print("No")
# else:
#     print("Yes")

ans = "Yes"
if C > D:
    tmp = S[B-2:D+1].count("...")
    if tmp == 0:
        ans = "No"

tmp = S[A-1:max(C, D)].count("##")
if tmp > 0:
    ans = "No"
print(ans)
