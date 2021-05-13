# Count ABC
N = int(input())
S = input()

ans = 0
for i in range(N-2):
    if i != N-2:
        ans += [0, 1]['ABC' == S[i:i+3]]
print(ans)
