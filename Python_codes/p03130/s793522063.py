a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())
a3, b3 = map(int, input().split())

li_w = [a1, b1, a2, b2, a3, b3]

result = [li_w.count(i) for i in range(1, 5)]
if result.count(2) == 2 and result.count(1) == 2:
    print("YES")
else:
    print("NO")
