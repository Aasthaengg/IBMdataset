n = int(input())
SMs = []
for i in range(2, n // 2 + 2):
    SMs.append(sum(list(map(int, str(i)))) + sum(list(map(int, str(n-i)))))
print(min(SMs))