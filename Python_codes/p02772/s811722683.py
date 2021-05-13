# ABC155
# B Papers,Please
n = int(input())
a = list(map(int, input().split()))
ans = 0
ant = 0
b = []
for i in range(n):
    if a[i] % 2 == 0:
        ant += 1
        b.append(int(a[i]))
        if a[i] % 3 == 0:
            ans += 1
        elif a[i] % 5 == 0:
            ans += 1

if ant == ans:
    if ant > 0:
        print("APPROVED")
    else:
        print("APPROVED")
else:
    print("DENIED")
