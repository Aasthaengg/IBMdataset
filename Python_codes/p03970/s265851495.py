string = 'CODEFESTIVAL2016'
s = input()
a = 0

for i in range(len(s)):
    if s[i] != string[i]:
        a += 1
print(a)