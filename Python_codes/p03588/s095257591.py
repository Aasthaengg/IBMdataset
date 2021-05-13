N = int(input())
AB = []
for i in range(N):
    a, b = list(map(int, input().split()))
    AB.append([a, b])

AB.sort(reverse=True, key=lambda x:x[0])
ans = AB[0][0] + AB[0][1]
print(ans)