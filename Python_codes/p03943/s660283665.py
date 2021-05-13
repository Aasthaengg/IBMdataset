A = list(map(int, input().split()))
if sum(A)%2:
    print("No")
    exit()
ave = sum(A)//2
if ave in A:
    print("Yes")
else:
    print("No")