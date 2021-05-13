S = input()
alphabet = "abcdefghijklmnopqrstuvwxyz"
if S == "zyxwvutsrqponmlkjihgfedcba":
    print(-1)
else:
    if len(S)<26:
        for a in alphabet:
            if a not in S:
                print(S + a)
                exit()
    else:#コイツを下回らない程度に辞書順を最低にする
        ordmax = 0
        for n,s in enumerate(reversed(S)):
            if ordmax > ord(s):

                for j in range(alphabet.index(s)+1,26):
                    if alphabet[j] not in S[:-n-1] :
                        print(S[:-n-1] + alphabet[j])
                        exit()
            else:
                ordmax = max(ordmax,ord(s))