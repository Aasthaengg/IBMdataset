N = int(input())
a = list(map(int,input().split()))
s = 0
for i in a:
    if i % 2 == 1:
        s += 1
if s % 2 == 0:
    print("YES")
else:
    print("NO")