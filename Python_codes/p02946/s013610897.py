# ABC137 B - One Clue

K,L = map(int,input().split())
T = []
for i in range(K):
    T.append(L-i)
for i in range(K):
    T.append(L+i)
    
T = list(set(T))

list.sort(T, reverse=False)
print(*T)