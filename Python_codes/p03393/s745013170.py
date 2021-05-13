S = input()
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in alphabet:
    if i not in S:
        print(S + i)
        break
else:
    output = False
    while len(S) > 0 and not output:
        last = alphabet.index(S[-1])
        for i in alphabet[last + 1:]:
            if i not in S[:-1]:
                print(S[:-1] + i)
                output = not(output)
                break
        else:
            S = S[:-1]
    if not output:
        print(-1)
