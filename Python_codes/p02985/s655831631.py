import queue
n,k = map(int,input().split())

ab = [[] for j in range(n+1)]
mod = 10**9 + 7

for i in range(n-1):
    a,b = map(int,input().split())
    ab[a].append(b)
    ab[b].append(a)
    
check = [False] * (n+1)
kazu = [0] * (n+1)

check[0] = True

q = queue.Queue()
q.put(1)

ans = k
#print(ab)

while not q.empty():
    tmp = q.get()
    check[tmp] = True
    kake = 0
    for i in range(len(ab[tmp])):
        if check[ab[tmp][i]] == True:
            continue
        kazu[ab[tmp][i]] += 1
        q.put(ab[tmp][i])
        ans *= k - kake - kazu[tmp] - 1
        ans %= mod
        #print(i,k,ans,tmp,kazu[tmp])
        kake += 1
    
print(ans)