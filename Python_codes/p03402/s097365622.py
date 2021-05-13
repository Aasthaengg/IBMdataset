import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())

A,B = MI()

q1,r1 = (B-1)//50,(B-1)%50
q1 += 1
q2,r2 = (A-1)//50,(A-1)%50
q2 += 1

if B > 1 and A > 1:
    print(2*(q1+q2),100)
elif (B == 1 and A > 1) or (B > 1 and A == 1):
    print(2*(q1+q2)-1,100)
else:
    print(2,100)

if B > 1:
    for i in range(2 * q1):
        if i % 2 == 1:
            print(''.join(['.'] * 100))
        elif i != 2 * q1 - 2:
            print(''.join(['.', '#'] * 50))
        else:
            print(''.join(['.', '#'] * r1 + ['.'] * (100 - 2 * r1)))
else:
    print(''.join(['.']*100))


if A > 1:
    for i in range(2 * q2):
        if i % 2 == 0:
            print(''.join(['#'] * 100))
        elif i != 2 * q2 - 1:
            print(''.join(['#', '.'] * 50))
        else:
            print(''.join(['#', '.'] * r2 + ['#'] * (100 - 2 * r2)))
else:
    print(''.join(['#']*100))
