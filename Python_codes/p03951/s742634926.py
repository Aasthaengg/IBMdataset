n = int(input())
S = input()
T = input()
cnt = 0
for i in range(n):
    if S[n - i - 1:] == T[: i + 1]:
        cnt = i + 1
print(2*n-cnt)