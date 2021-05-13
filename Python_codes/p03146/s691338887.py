s = int(input())

A = set()
while(True):
    if s in A:
        break    
    else:
        A.add(s)
        if s%2==0:
            s = s/2
        else:
            s = 3*s+1

print(len(A)+1)