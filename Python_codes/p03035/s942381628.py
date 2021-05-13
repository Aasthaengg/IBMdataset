res = [int(i) for i in input().split() if i.isdigit()]
if res[0] >= 6 and res[0] <= 12:
    print(int(res[1]/2))
elif res[0] <= 5:
    print(0)
elif res[0] >= 13:
    print(int(res[1]))
