
def Cukky(a,b):

    if a%2 == 0:
        a = a/2
    else:
        a = (a-1)/2

    b += a

    return a,b



A,B,K = map(int,input().rstrip().split(' '))

for i in range(K):
    if i%2 != 0:
        B,A = Cukky(B,A)
    else:
        A,B = Cukky(A,B)

print("{} {}".format(int(A),int(B)))