a = int(input())
S = 'abcdefghij'

def dfs(s,c):
    if c == a:
        ans.append(s)
        return 
    for i in S[:c+1]:
        if i in s:dfs(s+i,c+1)
        else:
            dfs(s+i,c+1)
            return 
ans = []

dfs("",0)

for i in ans:
    print(i)