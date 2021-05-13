inpl = lambda: list(map(int,input().split()))
N = int(input())
partners = []
for i in range(N):
    partners.append(set())
for i in range(N-1):
    a, b = inpl()
    a -= 1
    b -= 1
    partners[a].add(b)
    partners[b].add(a)
C = sorted(inpl())

def goto_leaf(k):
    prev_k = None
    while len(partners[k]) > 1:
        for p in partners[k]:
            if p != prev_k:
                break
        prev_k = k
        k = p
    return k

def delete_leaf(k):
    for stem in partners[k]:
        break
    partners[stem].remove(k)
    return stem

M = sum(C[:-1])
D = [0]*N
k = 0
for i in range(N-1):
    k = goto_leaf(k)
    D[k] = C[i]
    k = delete_leaf(k)
D[k] = C[N-1]

print(M)
print(' '.join(map(str,D)))