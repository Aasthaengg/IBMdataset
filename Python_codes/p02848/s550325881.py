N = int(input())
s = input()
S=''
for i in range(len(s)):
    a=ord(s[i])
    a+=N
    if a>ord('Z'):
        a-=26
    S+=chr(a)

print(S)