a, b = map(str,input().split())
ab = int(a+b)

for i in range(500):
    if ab == i*i:
        print("Yes")
        exit()

print("No")