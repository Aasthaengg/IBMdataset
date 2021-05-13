lst = list(map(int,input().split()))

S = sum(lst)

if S%9 == 0:
    print("Yes")
else:
    print("No")