N = int(input())
info = []
for i in range(N):
    b, a = map(int, input().split())
    info.append((a, b))
# print(info)
info.sort()

# print(info)
ans = sum(info[0])
print(ans)
