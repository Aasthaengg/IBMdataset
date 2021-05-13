coin = list(map(int,input().split()))
if coin[0] + coin[1] >= coin[2]:
    print("Yes")
else:
    print("No")