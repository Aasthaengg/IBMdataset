A,B,C=map(int,input().split())

if A==B:
    if B==C:
        flg=False
    else:
        flg=True
elif B==C:
    flg=True
elif A==C:
    flg=True
else:
    flg=False

if flg:
    print("Yes")
else:
    print("No")