N = int(input())
X = list(map(int, input().split()))
average = round(sum(X) / len(X))
health = 0
for x in X:
    health += (average - x)** 2
print(health)