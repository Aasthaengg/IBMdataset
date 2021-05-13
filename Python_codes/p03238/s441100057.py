N = int(input())

if N == 1:
    print("Hello World")
else:
    l = [int(input()) for _  in range(2)]
    print(l[0]+l[1])