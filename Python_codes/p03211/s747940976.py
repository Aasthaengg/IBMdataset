s = input()
n = len(s)

m = 1000

for i in range(n-2):
    m = min(m, abs(753 - int(s[i:i+3])))

print(m)