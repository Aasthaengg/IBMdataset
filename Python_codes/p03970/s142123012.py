s = "CODEFESTIVAL2016"
inp = input()
c = 0
for i in range(len(s)):
    if s[i] != inp[i]:
        c += 1
print(c)