A, B, C = map(int, input().split())
S = A+B+C

k = 0
flag = 0
while k<100:
    if A%2==1 or B%2==1 or C%2==1 or min([A,B,C])<1:
        flag = 1
        break
    An = (B + C)//2
    Bn = (A + C)//2
    Cn = (B + A)//2
    A = An 
    B = Bn 
    C = Cn         
    k += 1

if not flag:
    k = -1

print(k)