A = list(map(int,input().split()))
newA = sorted(A)

if newA[0]==newA[1]==newA[2]:
    print("No")
elif newA[0]  == newA[1] or newA[1] == newA[2]:
    print("Yes")
else:
    print("No")