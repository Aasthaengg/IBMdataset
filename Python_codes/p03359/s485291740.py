tmp = input().split(" ")
month = int(tmp[0])
day = int(tmp[1])

print(month) if day >= month else print(month - 1)