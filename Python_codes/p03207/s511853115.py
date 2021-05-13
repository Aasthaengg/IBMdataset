N = int(input())
p = []
for i in range(N):
    p.append(int(input()))
answer = sum(p) - max(p) // 2
print(answer)