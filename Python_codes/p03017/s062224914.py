N, A, B, C, D = map(int, input().split())
S = input()

if "##" in S[A - 1: C] or "##" in S[B - 1: D]:
    print("No")
    exit(0)

if C <= D:
    print("Yes")
    exit(0)

ans = False
for i in range(B - 1, D):
    if (S[i - 1] == '.') and (S[i] == '.') and (S[i + 1] == '.'):
        ans = True
        break

if ans:
    print("Yes")
else:
    print("No")
