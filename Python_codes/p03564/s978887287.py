N = int(input())
K = int(input())

min = float('inf')

def dfs(n, total):
    global N,K,min

    if n==N:
        if min>total:
            min = total
        return

    dfs(n+1, total*2)
    dfs(n+1, total+K)

dfs(0, 1)#n回目の操作で合計がtotal
print(min)