#0-indexed
n = int(input())
L = [[]*n for i in range(n)]
for i in range(n):
    a = int(input())
    for j in range(a):
        x,y = map(int,input().split())
        x-=1
        L[i].append((x,y))
#print(L)
ans = 0
for i in range(1<<n):
    bit = [(i>>j)&1 for j in range(n)]
    #print(bit)
    flag = True
    for j in range(n):
        if bit[j]:
            for x,y in L[j]:
                if bit[x] != y:
                    flag = False
                    break
            if not flag:
                break
    if flag:
        ans = max(ans,sum(bit))
print(ans)
