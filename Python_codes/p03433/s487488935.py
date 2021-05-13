N = int(input())
A = int(input())
temp = N%500
if temp<=A:
    print("Yes")
elif temp > A:
    print("No")