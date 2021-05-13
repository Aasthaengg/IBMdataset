n = int(input())
a = list(map(int, input().split()))

r = 0
m = 0
for i in a:
    if m <= i:
        m = i
    else:
        r += m-i
print(r)