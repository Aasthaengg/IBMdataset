A = [1,3,5,7,8,10,12]
B = [4,6,9,11]
C = [2]
D,E = list(map(int,input().split()))
if D in A and E in A:
    print("Yes")
    exit()
elif D in B and E in B:
    print("Yes")
    exit()
elif D in C and E in C:
    print("Yes")
    exit()
print("No")