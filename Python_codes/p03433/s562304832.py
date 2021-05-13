N=int(input())
A=int(input())

s=N%500

if s<=A:
    print("Yes")
    exit()

print("No")