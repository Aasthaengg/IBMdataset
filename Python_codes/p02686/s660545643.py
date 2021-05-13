n = int(input())
s = [0] * n
inc = []
zeros = []
dec = []

for i in range(n):
    s[i] = input()
    start = 0
    minimum = 0
    now = 0
    for c in s[i]:
        if c == '(':now += 1
        else: now -= 1
        minimum = min(minimum, now)
    end = now
    
    if end == 0:
        zeros.append((minimum, i))
    elif start < end:
        inc.append((minimum, i))
    else:
        minimum = minimum - end
        dec.append((minimum, i))

inc.sort(reverse=True)
dec.sort()


now = 0
for (m, i) in inc:
    for c in s[i]:
        if c == '(':now += 1
        else: now -= 1
        if now < 0:
            print("No")
            exit()
        
for (m, i) in zeros:
    for c in s[i]:
        if c == '(':now += 1
        else: now -= 1
        if now < 0:
            print("No")
            exit()

for (m, i) in dec:
    for c in s[i]:
        if c == '(':now += 1
        else: now -= 1
        if now < 0:
            print("No")
            exit()

if now != 0:
    print("No")
else:
    print("Yes")
