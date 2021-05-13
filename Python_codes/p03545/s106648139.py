from itertools import zip_longest

s = list(input())

for i in range(2**3) :
    lis = []
    c = ""
    for j in range(3) :
        if (i >> j) & 1 :
            lis.append("+")
        else:
            lis.append("-")
        
    for a, b in zip_longest(s, lis, fillvalue = "") :
        c += a + b
    
    if eval(c) == 7 :
        print(f"{c}=7")
        break