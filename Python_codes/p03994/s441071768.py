s = input()
k = int(input())
n = len(s)
le = [""]*n
ne = []

for i in range(n):
    le[i] = s[i]
    if s[i] == "a":
        ne.append(0)
    else:
        ne.append(123-ord(s[i]))
        
rem = k
for i in range(n):
    if rem >= ne[i]:
        rem -= ne[i]
        le[i] = 'a'
        
saigo = ord(le[n-1]) - 97
ssm = (rem+saigo) % 26
le[n-1] = chr(97+ssm)

print(*le,sep = "")