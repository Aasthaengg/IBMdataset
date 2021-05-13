S = input()
s = [True] * 26
for i in range(len(S)):
    if s[ ord(S[i]) - 97 ]:
        s[ ord(S[i]) - 97 ] = False
    else:
        print('no')
        exit()
print('yes')
