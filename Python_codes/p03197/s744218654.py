n=int(input())
a=[int(input()) for i in range(n)]

if all([i%2==0 for i in a]):
    print("second")
else:
    print("first")