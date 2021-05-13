#降参

n=int(input())
a=[int(input())%2 for _ in range(n)]

if 1 in a:
    print("first")
else:
    print("second")
