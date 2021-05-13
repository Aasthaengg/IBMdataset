S = input()
t = "CODEFESTIVAL2016"
a = 0
for i in range(16):
    if (t[i] != S[i]):
        a += 1

print(a)
