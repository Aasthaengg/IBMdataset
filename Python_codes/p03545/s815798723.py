import sys
a = list(str(input()))
#print(a)


for i in range(1 << 3):
    op = ['+']*3
    #range 3 because we need to look at all the bits
    for j in range(3):
        if (i >> j)&1:
            #starting from the right
            op[j] = "-"
    op.append('')        
    res = ''
    
    for x,y in zip(a,op):
        res += x+y
        
    if eval(res) == 7:
        print(res+'=7')
        sys.exit()