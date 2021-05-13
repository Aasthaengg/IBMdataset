n = int(input())
d = []
for i in range(n):
    d.append(int(input()))
ans = list(set(d))
print(len(ans))