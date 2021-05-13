A, B, K = map(int,input().split())
tmp = 0
Turn = "A"

def processing_A():
    global A,B,Turn,tmp
    tmp = A//2
    A = A//2
    B += tmp
    Turn = "B"
def processing_B():
    global A,B,Turn,tmp
    tmp = B//2
    B = B//2
    A += tmp
    Turn = "A"

for i in range(K):
    if Turn == "A":
        if A % 2 == 1:
            A -= 1
            processing_A()
        else:
            processing_A()
    else:
        if B % 2 == 1:
            B -= 1
            processing_B()
        else:
            processing_B()
print(A,B)