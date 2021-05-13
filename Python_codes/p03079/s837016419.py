n = [int(x) for x in input().split()]

res = 1 <= n[0] <= 100 and n[0] == n[1] == n[2]

if res:
    print("Yes")
else:
    print("No")