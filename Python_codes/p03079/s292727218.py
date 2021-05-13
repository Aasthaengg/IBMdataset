a = [int(i) for i in input().split()]
if len(set(a)) == 1:
    print("Yes")
else:
    print("No")