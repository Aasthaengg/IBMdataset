N, A, B, C, D = map(int, input().split())
S = input()

def solve():
    for i in range(A, C-3):
        if S[i:i+2] == "##":
            print("No")
            return
    for i in range(B, D-3):
        if S[i:i+2] == "##":
            print("No")
            return

    if C > D:
        for i in range(B-2, D-1):
            if S[i:i+3] == "...":
                print("Yes")
                return
        else:
            print("No")
            
    else:
        print("Yes")

solve()