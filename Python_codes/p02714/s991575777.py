N = int(input())
S = input()

count = S.count("R")*S.count("G")*S.count("B")

for i in range(len(S)-2):
    j = i + 1
    while len(S) > 2*j - i:
        k = 2*j - i
        if S[i] != S[j] and S[j] != S[k] and S[k] != S[i]:
            count -= 1
        j += 1

print(count)
