def INT():
    return int(input())

def MI():
    return map(int, input().split())

def LI():
    return list(map(int, input().split()))

N = INT()
ans = {}

for i in range(N):
    S, P = input().split()
    P = int(P)
    
    if S in ans.keys():
        ans[S].append([P, i + 1])
        ans[S].sort(key = lambda x : x[0], reverse = True)
    else:
        ans[S] = [[P, i + 1]]
    
store = list(ans.keys())
store.sort()

for s in store:
    for p in ans[s]:
        print(p[1])