l = list(input())
n = len(l)


for i in range(2**(n-1)):
    val = l[0]
    for j in range(n - 1):
        if (i >> j)&1 == 0:
            val += '-'
        elif (i >> j)&1 == 1:
            val += '+'
        
        val += l[j + 1]
    
    num = eval(val)
    if num == 7:
        print(val + '=7')
        break