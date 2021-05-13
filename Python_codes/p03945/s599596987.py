S = input()
answer = 0
present_color = ''
for i in range(len(S)):
    if i == 0:
        present_color = S[i]
        continue
    if present_color != S[i]:
        answer += 1
    else:
        pass
    present_color = S[i]
print(answer)
