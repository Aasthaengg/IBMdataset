S = input()
answer = 1000000
for i in range(len(S) - 2):
    answer = min(abs(753 - int(S[i:i + 3])), answer)
print(answer)
