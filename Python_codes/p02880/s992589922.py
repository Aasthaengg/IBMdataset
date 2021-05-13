n = int(input())

for x in range(1,10):
    for y in range(1,10):
        if x*y==n:
            print("Yes")
            exit()
    else:
        continue
    break
print("No")