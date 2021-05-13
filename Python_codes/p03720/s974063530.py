N, M = map(int, input().split())

citys = {i: 0 for i in range(1, N+1)}

for _ in range(M):
    a, b = map(int, input().split())
    citys[a] += 1
    citys[b] += 1
    
for num in citys.values():
    print(num)