n = 'CODEFESTIVAL2016'
s = input()
a = 0
for i in range(0, len(n)):
    if n[i] != s[i]:
        a+=1
print(a)