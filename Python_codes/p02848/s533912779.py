N = int(input())
S = input()
newS = ''
A = ord('A')
Z = ord('Z')
for k in range(len(S)):
    if ord(S[k]) + N > Z:
        newS += chr(ord(S[k]) + N - Z + A - 1)
    else:
        newS += chr(ord(S[k]) + N)
print(newS)
