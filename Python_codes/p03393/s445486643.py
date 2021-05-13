
S = input()
def aaa(S):

    Alphabet = "abcdefghijklmnopqrstuvwxyz"

    if len(S) == 26:
        j = 0
        for i in reversed(range(26)):
            while S[i] != Alphabet[j]:
                j = j + 1
                if j == 26:
                    k = 0
                    while S[i] != Alphabet[k]:
                        k += 1
                    while not Alphabet[k] in S[i+1:]:
                        k += 1
                    return S[:i] + Alphabet[k]                
        return -1

    else:
        for i in range(len(Alphabet)):
            j = 0
            while Alphabet[i] != S[j]:
                j += 1
                if j == len(S):
                    return S + Alphabet[i]

print(aaa(S))