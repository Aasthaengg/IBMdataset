S = input()
s = list(S)
o = [ord(x) for x in S]
alphabets = set([chr(i+97) for i in range(26)])
if len(S) < 26:
    used = set(s)
    unused = alphabets - used
    unusedo = [ord(x) for x in unused]
    print(''.join(S)+chr(min(unusedo)))
else:
    if S == 'zyxwvutsrqponmlkjihgfedcba':
        print('-1')
    else:
        diff = [ord(s[i+1]) - ord(s[i]) for i in range(25)]
        for i in range(1,26):
            if diff[-i] > 0:
                removed = S[:-i-1]
                current = S[-i-1]
                break
        usedr = set(list(removed)) | set(current)
        unusedr = alphabets - usedr
        unusedro = [ord(x) for x in unusedr if ord(x) > ord(current)]
        print(removed+chr(min(unusedro)))