n = int(input())
A = list(map(int,input().split()))
B = A.copy()
A.sort()

ans_ato = A[n//2]
ans_mae = A[n//2-1]

for b in B:
    if b < ans_ato:
        print(ans_ato)
    else:
        print(ans_mae)