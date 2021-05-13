A = list(input())
B = list(input())
C = list(input())
s = A.pop(0)
while True:
    if A == [] and s == 'a':
        print('A')
        exit()
    elif B == [] and s == 'b':
        print('B')
        exit()
    elif C == [] and s == 'c':
        print('C')
        exit()
    if s == 'a':
        s = A.pop(0)
    elif s == 'b':
        s = B.pop(0)
    elif s == 'c':
        s = C.pop(0)