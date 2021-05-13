N = int(input())
es = [[] for _ in range(N)]
for i in range(N-1):
    a,b = map(int, input().split())
    es[a-1].append(b-1)
    es[b-1].append(a-1)

C = list(map(int, input().split()))
C.sort(reverse=True)
D = [0 for _ in range(N)]
stack = es[0]
D[0] = C[0]
cnt_c = 1
while stack:
    new_stack = []
    for i in stack:
        if D[i] == 0:
            D[i] = C[cnt_c]
            cnt_c += 1
            new_stack.extend(es[i])
    if len(new_stack) == 0:
        break
    else:
        stack = new_stack

print(sum(D) - C[0]) # ｃの最大のやつは辺の値になれないので引く
print(*D)