N = int(input())
A = int(input())
1 <= N <= 10000
0 <= A <= 1000
if N < 500 and N == A:
    print("Yes")
elif A >= N%500:
    print("Yes")
else:
    print("No")