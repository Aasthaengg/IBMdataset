N = int(input())

bridge = []
for i in range(1, N):
    for j in range(i + 1, N + 1):
        if(N % 2 == 0):
            if(i + j == N + 1):
#                print("skip = [{}, {}]".format(i,j))
                continue
        else:
            if(i + j == N):
#                print("skip = [{}, {}]".format(i,j))
                continue
        bridge.append([i, j])

print(str(len(bridge)))
for i in bridge:
    print(" ".join(map(str, i)))
