ab = int(input().replace(" ",""))

for i in range(320):
    j = i ** 2
    if j == ab:
        print("Yes")
        exit()
print("No")