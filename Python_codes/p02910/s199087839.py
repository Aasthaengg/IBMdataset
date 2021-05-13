S = input()
val = True
for i in range(1, len(S) + 1):
    if i % 2 and (S[i - 1] in ['R', 'U', 'D']):
        pass
    elif i % 2 == 0 and (S[i - 1] in ['L', 'U', 'D']):
        pass
    else:
        val = False
    if not val:
        print('No')
        break
else:
    print('Yes')