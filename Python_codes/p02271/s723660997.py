def check(m,g,A,n):
    
    for i in range(n):
        gg = g + A[n-i-1]
        if m == gg:
            return True
        elif n == 0 or m < gg:
            continue
        if check(m,gg,A,n-i-1) == True:
            return True
    return False
        

    

n=int(input())
A=list(map(int,str.split(input())))
q = int(input())
m=list(map(int,str.split(input())))




mini = min(A)
nor = sum(A)

for mi in m:
    if mi < mini or mi > nor:
        print("no")
        continue
    if check(mi,0,A,n):
        print("yes")
    else:
        print("no")