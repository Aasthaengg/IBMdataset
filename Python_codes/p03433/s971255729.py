N,A = [int(input().rstrip()) for i in range(2)]
if N-int(N/500)*500 <= A:
    print("Yes")
else:
    print("No")
