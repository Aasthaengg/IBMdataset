n = list(input())

for i in range(3):
    #print(n[i])
    if n[i]=='1':
        n[i]='9'
    else:
        n[i]='1'

print(int(''.join(n)))