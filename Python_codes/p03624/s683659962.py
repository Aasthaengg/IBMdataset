S = input()
s = [ True ] * 26
for i in range(len(S)):
    s[ord(S[i])-97] = False
for i in range(26):
    if s[i]:
        print(chr(i+97))
        exit()
print(None)
