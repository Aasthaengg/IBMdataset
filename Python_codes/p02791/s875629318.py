n = int(input())
p = list(map(int, input().split()))
num = 1
mini = p[0]
for i in range(1,n):
    if p[i] < mini:
        num += 1
        mini = p[i]
print(num)