a, b, x = map(int, input().split())
count = 0
for i in range(max(a,b),0,-1):
    if a % i == 0 and b % i == 0:
        count += 1
    if count == x:
        break
print(i)