A,B,C,D=map(int,input().split())

def ans164(A, B, C, D):
    while True:
        C=C-B
        if A<=0:
            return"No"
            break
        A=A-D
        if C<=0:
            return "Yes"
            break

print(ans164(A,B,C,D))