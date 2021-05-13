from queue import Queue

N = int(input())
node_array = [[] for i in range(N)]

for _ in range(N - 1):
    i, j = map(int, input().split())
    node_array[i - 1].append(j - 1)
    node_array[j - 1].append(i - 1)

c_array = sorted(map(int, input().split()), reverse=True)
ans = sum(c_array[1:])
ans_array = [-1] * N

edge = Queue()

edge.put(0)
ans_array[0] = 0

for i in range(N):
    item = edge.get()
    ans_array[item] = str(c_array[i])
    for j in node_array[item]:
        if ans_array[j] == -1:
            edge.put(j)
            ans_array[j] == 0

print(ans)
print(" ".join(ans_array))
