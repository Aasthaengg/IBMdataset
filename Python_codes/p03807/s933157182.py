n = int(input())
a = list(map(int, input().split(" ")))
even = []
odd = []
for i in a:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

ans = "YES"
if len(odd) % 2 == 1:
    ans = "NO"
print(ans)