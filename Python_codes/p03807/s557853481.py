n = int(input())
a = list(map(int, input().split()))
c = 0
for i in a:
    if i & 1:
        c += 1
if c & 1 == 0:
    print("YES")
else:
    print("NO")