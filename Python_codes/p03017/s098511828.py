N, A, B, C, D = map(int, input().split())
s = input()

if C > D:
    if "##" in s:
        print("No")
    else:
        if "..." in s[B-2:D+1]:
            print("Yes")
        else:
            print("No")
else:
    if "##" in s[min(A,B)-1:D]:
        print("No")
    else:
        print("Yes")