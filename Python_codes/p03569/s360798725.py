S = input()
i = 0
j = len(S) - 1
cnt = 0

while i < j:
    if S[i] == S[j]:
        i += 1
        j -= 1
    elif S[i] == 'x':
        cnt += 1
        i += 1
    elif S[j] == 'x':
        cnt += 1
        j -= 1
    else:
        print(-1)
        exit()
print(cnt)
