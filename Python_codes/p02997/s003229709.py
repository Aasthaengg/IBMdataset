import sys

N, K = map(int, input().split())

if K > (N-1)*(N-2)//2:
    print(-1)
    sys.exit()

edges = [(1, v) for v in range(2, N+1)]

num = (N-1)*(N-2)//2
for u in range(2, N+1):
    for v in range(u+1, N+1):
        if num == K:
            break
        edges.append((u, v))
        num -= 1
    else:
        continue
    break

print(len(edges))
print('\n'.join(map(lambda x: str(x[0])+' '+str(x[1]), edges)))
