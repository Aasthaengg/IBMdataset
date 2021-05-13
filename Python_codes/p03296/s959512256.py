n=int(input())
a = [int(i) for i in input().split()]
ans = 0
b = 0
j = -1
for i in a:
    if i != j:
        ans += b // 2
        b=1
    else:
        b += 1
    j = i
ans += b // 2

print(ans)