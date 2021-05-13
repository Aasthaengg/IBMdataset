H,W = map(int,input().split())
pic = []

for i in range(H):
    pic.append("#" + input() + "#")

print("#"*(W+2))

for i in pic:
    print(i)

print("#"*(W+2))