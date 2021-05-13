i = [int(s) for s in input().split()]
m = max(i)
i.remove(m)
a = i[0] + i[1]

if a == m:
    print("Yes")
else:
    print("No")
