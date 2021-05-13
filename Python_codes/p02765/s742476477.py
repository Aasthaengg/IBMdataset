n,dr = map(int, input().split())

if n>= 10:
    ir=dr
    
else:
    ir = dr + 100*(10-n)
    
print(ir)