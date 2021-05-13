a = list(map(int, input().split()))
s = 0

for i in a:
    s += i

if s >= 22:
    print("bust")
else:
    print("win")