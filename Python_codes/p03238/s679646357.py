n=int(input())

if n==1:
    print("Hello World")
else:
    l=[int(input()) for _ in range(2)]
    print(sum(l))