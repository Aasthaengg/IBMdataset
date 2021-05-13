s = input()
bkt = [0 for _ in range(26)]
for i in range(len(s)):
    bkt[ord(s[i])-97] = 1
print('None' if sum(bkt) == 26 else chr(bkt.index(0) + 97))