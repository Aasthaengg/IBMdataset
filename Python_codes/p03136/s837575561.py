def resolve():
    N = int(input())
    L = [int(i) for i in input().split()]
    if max(L) < (sum(L) - max(L)):
        print("Yes")
    else:
        print("No")


resolve()
