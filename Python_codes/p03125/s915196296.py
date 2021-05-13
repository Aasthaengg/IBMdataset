from sys import stdin
sp = stdin.readline().split()
A, B = int(sp[0]), int(sp[1])

def div(num):
    l = []
    for itr in range(1,num+1):
        if num % itr == 0:
            l.append(itr)
    return l

B_divisor = div(B)
if A in B_divisor:
    print(A+B)
else:
    print(B-A)