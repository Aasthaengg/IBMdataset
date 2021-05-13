s = input()
K = int(input())

N = len(s)
words = set()
for i in range(N):
    for j in range(i+1, i+K+1):
        w = s[i:j]
        if w not in words:
            words.add(w)

print(sorted(list(words))[K-1])
