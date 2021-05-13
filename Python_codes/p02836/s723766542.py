S = str(input())
N = len(S) // 2
count = 0
for i in range(N):
    count += (S[i] != S[- i - 1]) * 1
print(count)