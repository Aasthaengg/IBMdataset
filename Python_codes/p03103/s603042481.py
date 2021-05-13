N, M = map(int, input().split())
List = []
for _ in range(N):
    A, B = map(int, input().split())
    List.append((A, B))
List.sort(key=lambda x: x[0])
Res = 0
for i in range(N):
    A, B = List[i]
    if B <= M:
        M -= B
        Res += A*B
    else:
        Res += A*M
        break
print(Res)