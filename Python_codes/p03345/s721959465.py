A,B,C,K = map(int,input().split())

for i in range(K%2):
    tmp1 = A+B
    tmp2 = A+C
    tmp3 = B+C

    A = tmp3
    B = tmp2
    C = tmp1
if abs(A-B)>=10**18:
    print("Unfair")
else:
    print(A-B)