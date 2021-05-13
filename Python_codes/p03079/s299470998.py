int_arr = list(map(int,input().split()))
A = int_arr[0]
B = int_arr[1]
C = int_arr[2]

if A == B & B == C:
    print("Yes")
else:
    print("No")