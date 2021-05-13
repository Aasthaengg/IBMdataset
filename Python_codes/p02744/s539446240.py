N = int(input())
 
alp = "abcdefghijklmnopqrstuvwxyz"
 
def dfs(s):
    i = len(s)
    if i == N:
        print(s)
    else:
        index = 0
        for k in range(len(s)):
            index = max(index, alp.index(s[k]))
        for j in range(index+2):
            dfs(s+alp[j])
 
dfs("a")
