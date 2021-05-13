A,B,C=map(int,input().split())
if B/A<0:
    print(0)
elif B/A>=C:
    print(C)
else:
    print(int(B/A))