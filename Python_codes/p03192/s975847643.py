n = int(input())
li = []
while n > 0:
    li.append(n%10)
    n //= 10
li.reverse()
ans = 0
for i in range(len(li)):
    if li[i] == 2:
        ans += 1
print(ans)