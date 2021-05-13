S = list(input())
T = list(input())
pos = []
for i in range(len(S)-len(T)+1):
    if S[i] == T[0] or S[i] == '?':
        flag = 1
        for j in range(len(T)):
            if not T[j] == S[i+j] and not S[i+j] == '?':
                flag = 0
                break
        if flag:
            pos.append(i)

if not pos:
    print('UNRESTORABLE')
    exit()

words = []
for p in pos:
    word = S[0:p] + T + S[p+len(T):]
    for i in range(len(word)):
        if word[i] == '?':
            word[i] = 'a'
    words.append(word)
words.sort()
print("".join(words[0]))
