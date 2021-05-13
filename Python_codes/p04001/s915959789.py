s = input()
n = len(s)
sum = 0
for b in range(1 << (n-1)):
    t = 0
    for i in range(n-1):
        if b & (1 << i):
            sum += int(s[t:i+1])
            t = i+1
    sum += int(s[t:])
print(sum)