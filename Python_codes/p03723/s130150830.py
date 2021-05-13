A, B, C = map(int,input().split())

empty = [0] * 3
count = 0
if A == B == C and A % 2 == 0 and B % 2 == 0 and C % 2 == 0:
    print(-1) 
elif (A % 2 != 0) or (B % 2 != 0) or (C % 2 != 0):
    print(0)
else:
    while A % 2 == 0 and B % 2 == 0 and C % 2 == 0: 
        count += 1
        A_ = A//2
        B_ = B//2
        C_ = C//2
        A = B_ + C_
        B = A_ + C_
        C = A_ + B_

    print(count)