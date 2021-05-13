n = input()
a = int(n[-1])
b = 10 - int(n[-1])

for i in range(len(n)-2,-1,-1):
    a,b = min(a+int(n[i]), b + int(n[i]) + 1), min(a + 10-int(n[i]), b + 9 -int(n[i]))

print(min(a,b+1))