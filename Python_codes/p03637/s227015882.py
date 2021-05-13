n = int(input())
a = list(map(int, input().split()))
two = 0
four = 0

for i in a:
    if i%4 == 0:
        four += 1
    elif i%2 == 0:
        two += 1

if n == two:
    print("Yes")
elif four/(n - two) >= 0.5:
    print("Yes")
elif four/(n - 1) >= 0.5:
    print("Yes")
else:
    print("No")