N, A, B, C, D = map(int, input().split())
S = input()

from sys import exit

# check
goal = max(C, D)
if "##" in S[A-1:goal]:
    print("No")
    exit()

if C < D:
    # Bから先に動く
    print("Yes")

else:
    # 入れ替わる必要がある

    # cehck : 初期値で入れ替えられる
    if "..." in S[B-2:D+1]:
    # if ('...' in S[B-1:D]) or ('...' in S[B-2:B+1]) or ('...' in S[D-2:D+1]):
        print("Yes")
    else:
        print("No")