class rightnumber():
    def __init__(self):
        self.top = [[0, 0, 0, 0], [4, 2, 3, 5], [4, 6, 3, 1], [1, 2, 6, 5], [1, 5, 6, 2], [1, 3, 6, 4], [4, 5, 3, 2]]
        self.front =[[0, 0, 0, 0], [2, 3, 5, 4], [6, 3, 1, 4], [2, 6, 5, 1], [5, 6, 2, 1], [3, 6, 4, 1], [5, 3, 2, 4]]
inp = list(map(int, input().split()))
q = int(input())
rightnumbers = rightnumber()
top= [0]*q
front = [0]*q
key1 = [0]*q
key2 = [0]*q
for n in range(q):
    top[n], front[n] = map(int, input().split())
    for k in range(6):
        if top[n] == inp[k]:
            key1[n] = k;
        if front[n] == inp[k]:
            key2[n] = k
for n in range(q):
    for i in range(1, 7):
        for j in range(0, 4):
            if rightnumbers.top[i][j] == key1[n]+1 and rightnumbers.front[i][j] == key2[n]+1:
                print(inp[i-1])
