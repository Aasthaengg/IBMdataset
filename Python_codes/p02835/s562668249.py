a = list(map(int,input().split()))

print("win" if a[0]+a[1]+a[2] <= 21 else "bust")