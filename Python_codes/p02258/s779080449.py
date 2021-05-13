res = -10 ** 9
n   = int(input())
a   = int(input())
Min = int(a)

for mak in range(n - 1) :
    tem = 0
    b = int(input())
    Min = min(b, Min)
    
    if   b < a : tem = b - a
    else       : tem = b - Min

    if tem > res : res = int(tem)
    a   = int(b)
print(res)