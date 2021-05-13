N = int(input())
AB, ans = [], 0
for _ in range(N):
    a, b = map(int, input().split())
    AB.append([a+b, a, b])    
AB = sorted(AB, reverse=True)

for i in range(N):
    ans += (-1)**(i%2) * AB[i][i%2 + 1]
print(ans)