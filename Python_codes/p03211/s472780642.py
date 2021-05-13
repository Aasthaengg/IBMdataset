s = str(input())
a = 10000
for i in range(len(s) - 1):
    a = min(a, abs(753 - int(s[i:i+3])))
print(a)