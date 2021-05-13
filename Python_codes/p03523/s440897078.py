from sys import setrecursionlimit

setrecursionlimit(10**5)
S = input()
li = []
str = 'AKIHABARA'
def dfs(i, s):
    if i == len(str):
        li.append(s)
        return
    if str[i] == 'A':
        dfs(i+1, s)
    dfs(i+1, s+str[i])

dfs(0, '')
# print(li)
print('YES' if S in li else 'NO')

