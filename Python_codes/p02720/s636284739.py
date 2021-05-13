k = int(input())
lunlun = []
def dfs(A):
    if len(A) == 10:
        return
    else:
        start = int(A[-1])
        if start == 9:
            for i in range(start-1, start+1):
                A.append(str(i))
                lunlun.append("".join(A))
                dfs(A)
                A.pop()
        elif start == 0:
            for i in range(start, start+2):
                A.append(str(i))
                lunlun.append("".join(A))
                dfs(A)
                A.pop()
        else:
            for i in range(start-1, start+2):
                A.append(str(i))
                lunlun.append("".join(A))
                dfs(A)
                A.pop()
for j in range(1, 10):
    lunlun.append(str(j))
    dfs([str(j)])
lunlun = list(map(int, lunlun))
lunlun.sort()
print(lunlun[k-1])