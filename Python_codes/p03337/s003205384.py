l = list(map(int, input().split()))
a = l[0]
b = l[1]

ans1 = a + b
ans2 = a - b
ans3 = a * b

print(max(ans1, ans2, ans3))