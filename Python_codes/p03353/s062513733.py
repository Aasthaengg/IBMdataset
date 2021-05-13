import bisect
ALP = 'abcdefghijklmnopqrstuvwxyz'

S = input()
K = int(input())

N = len(S)
substr = []
for i in range(N):
    for j in range(i, min(i + 5, N)):
        tmp_substr = S[i:j+1]

        if tmp_substr in substr:
            continue

        if len(substr) <= 4:
            substr.append(tmp_substr)
            substr.sort()
        else:
            substr.append(tmp_substr)
            substr.sort()
            del substr[-1]

print(substr[K-1])