s = str(input())
n = 4
for bit in range(1 << (n-1)):
    f = s[0]
    for i in range(0,(n-1)):
        if bit & (1 << i):
            f += '+-' + s[i+1]
        else:
            f += '+' + s[i+1]
    #print(f)
    ans = sum(map(int,f.split('+')))
    if ans == 7:
        break
print(f.replace('+-','-')+'=7')
