n = int(input())
x = [list(map(int, input().split())) for _ in range(n)]
x.sort(key=lambda x:x[0])
worst = x[-1]

print(worst[0] + worst[1])