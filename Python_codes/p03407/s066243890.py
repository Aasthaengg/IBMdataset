inp = list(map(lambda x:int(x), input().split()))

if inp[2] <= inp[0] + inp[1]:
    print("Yes")
else:
    print("No")

