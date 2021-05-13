alpha = "abcdefghij"
n = int(input())
def dfs(s,k):
    if len(s) == n:
        print(s)
    else:
        for i in range(k+1):
            if i == k:
                dfs(s+alpha[i],k+1)
            else:
                dfs(s+alpha[i],k)
dfs("",0)