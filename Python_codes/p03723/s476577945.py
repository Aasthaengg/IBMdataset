A,B,C = map(int,input().split())

ans = 0

while True:
    if A%2!=0 or B%2!=0 or C%2!=0:
        print(ans)
        break
    elif A%2==0 and B%2==0 and C%2==0 and A == B == C:
        print('-1')
        break
    A_ = A/2
    B_ = B/2
    C_ = C/2
    A = B_+C_
    B = A_+C_
    C = A_+B_
    ans += 1
