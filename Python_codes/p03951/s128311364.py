n = int(input())
s = input()
t = input()

for i in range(len(s)):
    if s[i] != t[0]: continue
    if s[i:] == t[:len(s)-i]:
        print(i+len(t))
        exit()
print(len(s)+len(t))