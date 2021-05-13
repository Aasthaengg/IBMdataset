#26
H = int(input())
cou = 1
while H>0:
    H = int(H/2)
    cou *= 2
    
print(cou-1)