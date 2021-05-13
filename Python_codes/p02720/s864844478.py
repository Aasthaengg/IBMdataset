k = int(input())

al = []
def f(d, v, al):
    
    al.append(v)
    
    if d == 10:
        return
    
    for i in range(-1,2):
        add = (v%10) + i
        if add >= 0 and add <= 9:
            f(d+1, v*10+add, al)
            
            
for i in range(1,10):
    f(0, i, al)
    
al = sorted(al)

print(al[k-1])