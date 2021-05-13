N, A, B, C, D = map(int, input().split())
S = input()
canA = "##" not in S[A-1:C]
canB = "##" not in S[B-1:D]
if C < D:
    if canA and canB:
        print("Yes")
    else:
        print("No")
else:
    if canA and canB and ("..." in S[B-2:D+1]):
        print("Yes")
    else:
        print("No")
