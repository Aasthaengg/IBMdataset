S = input()
ng = False
for i, c in enumerate(S):
    if ((i + 1) % 2 == 0 and c == 'R') or ((i + 1) % 2 == 1 and c == 'L'):
        ng = True
        break
if ng:
    print('No')
else:
    print('Yes')
