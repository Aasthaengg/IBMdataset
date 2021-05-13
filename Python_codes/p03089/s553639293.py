import sys
sys.setrecursionlimit(10**6)

n = int(input())
b = list(map(int , input().split()))

def dfs(s, ans):
    if len(s) == 0:
        print('\n'.join(map(str, reversed(ans))))
        exit()
        return
    for i in range(len(s)):
        #if s[i] == i+1:
        #if s[i] == i+1 and max(s[:i] + [0]) >= i:
        if s[i] == i+1:
            s1 = s[:i] + s[i+1:]
            allok = True
            for j in range(len(s1)):
                if s1[j] > j+1:
                    allok = False
                    break
            #print(s[:i], s[i+1:],i)
            if allok:
                ans.append(s[i])
                dfs(s1, ans)
    if len(ans) > 0:
        ans.pop()

dfs(b, [])

print('-1')
