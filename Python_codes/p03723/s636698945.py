A,B,C=map(int,input().split())
initial = list([A, B, C])
initial.sort()
n=0
while True:
    if A%2==0 and B%2==0 and C%2==0:
        n+=1
        A_half = A//2
        B_half = B//2
        C_half = C//2
        A = B_half + C_half
        B = C_half + A_half
        C = A_half + B_half
        now = list([A, B, C])
        now.sort()
        if now == initial:
            n = -1
            break
    else:
        break

print(n)
