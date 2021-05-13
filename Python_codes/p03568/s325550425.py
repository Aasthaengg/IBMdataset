n = int(input())
a = list(map(int, input().split()))
x = 1
for i in a:
    if i % 2 == 0:
        x *=2
    else:
        x *=1
ans = 3**n -x
print(ans)