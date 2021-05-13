s = input()
cf = "CODEFESTIVAL2016"
t = 0
for i in range(16):
    t += 1 if s[i] != cf[i] else 0
print(t)
