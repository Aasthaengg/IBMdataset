s = input()
S = ''.join(list(reversed(s)))
N = len(S)

i = 0
while True:
    l = N - i
    if l>=5 and (S[i:i+5]=='maerd' or S[i:i+5]=='esare'):
        i += 5
    elif l>=6 and S[i:i+6]=='resare':
        i += 6
    elif l>=7 and S[i:i+7]=='remaerd':
        i += 7
    else:
        print("NO")
        exit()
    if i == N:
        print('YES')
        exit()
