N, M = map(int, input().split())
array = sorted([list(map(int, input().split()))
                for i in range(M)], key=lambda x: x[1])

# print(array)
count = 0
position = -float("inf")
for i in range(M):
    if array[i][0] < position:
        pass
    else:
        position = array[i][1]
        count += 1
print(count)
