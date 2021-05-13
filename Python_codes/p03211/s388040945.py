import itertools
S = input()
num_lis = []

s = 0
for _ in range(0, len(S)-2):
    num = int(S[s:s+3])
    num_lis.append(abs(753-num))
    s += 1

print(min(num_lis))
