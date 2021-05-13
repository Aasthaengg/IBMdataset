n = int(input())
t, a = map(int, input().split())
l = list(map(int, input().split()))
ans = 0
minNum = float('inf')

for i in range(len(l)):
    num = t - l[i] * 0.006
    if abs(num - a) < minNum:
        minNum = abs(num -a)
        ans = i + 1
print(ans)