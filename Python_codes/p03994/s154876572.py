s = input()
K = int(input())
s = list(s)

# print(diff)

for i in range(len(s)):
    if s[i] != 'a':
        dist = ord('z') - ord(s[i]) + 1
        if dist <= K:
            K -= dist
            s[i] = 'a'
# print(s)
temp = K % 26
s[-1] = chr(ord(s[-1]) + temp)
# print(s)

print(''.join(s))


