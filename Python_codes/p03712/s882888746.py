H, W = map(int,input().split())
pic = []
for i in range(H):
    pic.append(list(map(str, input().split())))

print("#" * (W + 2))
for j in range(H):
    print("#" + pic[j][0] + "#")
print("#" * (W + 2))