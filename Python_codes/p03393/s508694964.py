S = input()

if S == "".join([chr(i) for i in reversed(range(97, 97 + 26))]):
    print(-1)
    exit()

M = 96
for i in range(97, 97 + 26):
    if not chr(i) in S:
        M = i
        break
if M != 96:
    print(S + chr(M))
    exit()

unused = [False] * 128
for i in reversed(range(len(S))):
    for j in range(ord(S[i]) + 1, 97 + 26):
        if unused[j]:
            print(S[0:i] + chr(j))
            exit()
    unused[ord(S[i])] = True