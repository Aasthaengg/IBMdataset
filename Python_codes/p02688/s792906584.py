n,k = map(int, input().split())
array = [0] * n
for i in range(k):
    d = int(input())
    l = list(map(int, input().split()))
    for j in l:
        array[j-1] = 1
ans = 0
for i in range(len(array)):
    if array[i] == 0:
        ans += 1
print(ans)

