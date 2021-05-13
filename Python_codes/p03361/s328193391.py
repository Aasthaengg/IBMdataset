h,w = map(int, input().split())
lis = []

for i in range(h):
    lis.append(list(input()))

for i in range(1,h-1):
    for j in range(1,w-1):
        if lis[i][j] == "#":
            if lis[i-1][j] == "." and lis[i+1][j] == "." and lis[i][j-1] == "." and lis[i][j+1] == ".":
                print("No")
                exit()

print("Yes")