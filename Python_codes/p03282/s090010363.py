s = list(input())
k = int(input())

for i in range(min(k,len(s))):
    if s[i] != '1':
        print(s[i])
        exit(0)

print(1)