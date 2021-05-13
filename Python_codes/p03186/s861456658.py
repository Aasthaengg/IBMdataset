A,B,C = map(int,input().split())
if B>=C:
    print(C+B)
else:
    a = 2*B+min(C-B,A)
    if C-B-A>=1:
        a += 1
    print(a)