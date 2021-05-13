S = input()
N = len(S)
K = int(input())
ngrams = set(S)
for n in range(2, 6):
    for i in range(N - n + 1):
        ngrams.add(S[i:i + n])
print(sorted(ngrams)[K - 1])