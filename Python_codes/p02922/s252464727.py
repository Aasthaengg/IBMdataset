num = list(input().split()) 
a = int(num[0])
b = int(num[1])
ans = 0
tap = 1
while b > tap:
    tap += a-1
    ans += 1

print(ans)