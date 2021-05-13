S = input()
answer = 0
s = 'CODEFESTIVAL2016'

for i in range(len(S)):
    if S[i] != s[i]:
        answer += 1

print(answer)