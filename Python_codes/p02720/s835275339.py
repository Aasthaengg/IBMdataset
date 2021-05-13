k = int(input())
lunlun = []
def dfs(A):
    if len(A) > 10:
        return 
    else:
        num = int(A[-1])
        lunlun.append(int("".join(A)))
        if num == 0:
            for i in range(0, 2):
                A.append(str(i))
                dfs(A)
                A.pop()
        elif num == 9:
            for i in range(8, 10):
                A.append(str(i))
                dfs(A)
                A.pop()
        else:
            for i in range(num-1, num+2):
                A.append(str(i))
                dfs(A)
                A.pop()

for i in range(1, 10):
    dfs([str(i)])
lunlun.sort()
print(lunlun[k-1])