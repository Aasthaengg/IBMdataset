s=input()
if len(s)>10:
    print('NO')
    exit()

for bit in range(2**(len(s)+1)):
    T = ""
    for j in range(len(s)+1):
        if ((bit >> j) & 1):
            T += "A"
        if j<(len(s)):
            T += s[j]
    if T=='AKIHABARA':
        print('YES')
        exit()

print('NO')    