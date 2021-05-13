t = input()
answer = []
for idx, w in enumerate(t):
    if w in ['P', 'D']:
        answer.append(w)
    else:
        if len(answer) != 0 and answer[-1] == 'P':
            answer.append('D')
        else:
            if idx == len(t) - 1:
                answer.append('D')
            elif t[idx + 1] in ['D', '?']:
                answer.append('P')
            else:
                answer.append('D')
print(''.join(answer))
