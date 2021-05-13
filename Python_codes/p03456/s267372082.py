n=int(input().replace(" ",""))
for i in range(10000):
    if i**2==n:
        print("Yes")
        exit()
print("No")