n = int(input())
a = [None]
for i in range(n):
    adj = list(map(int,input().split()))
    a.append(adj[2:])
    
s = [None]
for i in range(1, n + 1):
    s.append([False, i])
    
time = 0

def dfs(u):
    global time
    s[u][0] = True
    time += 1
    s[u].append(time)
    
    for v in a[u]:
        if s[v][0] == False:
            dfs(v)
            
    time += 1
    s[u].append(time)
    
for i in range(1,n+1):
    if s[i][0] == False:
        dfs(i)
        
for x in s[1:]:
    print(*x[1:])
