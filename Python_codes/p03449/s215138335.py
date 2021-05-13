n = int(input())
apple = []
for _ in range(2):
    apple.append(list(map(int, input().split())))
orange = []
for i in range(n):
    a = apple[0]
    b = apple[1]
    orange.append(sum(a[0:i+1] + b[i:n]))
print(max(orange))
