n = int(input())
a_list = [0 for _ in range(n)]
for i in range(n):    
    a_list[int(input()) - 1] = i
length = 1
ans = 0
prev = a_list[0]
for i in range(n - 1):
    if (a_list[i + 1] - prev) >= 1:
        length += 1
    else:
        ans = max(length, ans)
        length = 1
    prev = a_list[i + 1]
ans = max(length, ans)
print(n - ans)