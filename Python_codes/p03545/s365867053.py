import itertools
s = input()
ans=0
for i in list(itertools.product([0,1], repeat=len(s)-1)):
    b = 0
    a = int(s[0])
    l = [a]+[0]*(2*(len(s)-1))
    for j in range(len(s)-1):
        if i[j] == 0:
            a += int(s[j+1])
            l[2*j+1] = '+'
            l[2*j+2] = str(s[j+1])
        else:
            a -= int(s[j+1])
            l[2*j+1] = '-'
            l[2*j+2] = str(s[j+1])
    if a == 7:
        l[0] = str(s[0])
        l += '=7'
        l = ''.join(l)
        print(l)
        break