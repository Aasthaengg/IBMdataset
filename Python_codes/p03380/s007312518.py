n = int(input())
l = list(map(int, input().split()))

l.sort()
ans1 = l[-1]
ans2 = -1
diff = 1000000000
for i in range(n-1):
    if diff >= abs(l[i] - ans1//2):
        ans2 = l[i]
        diff = abs(l[i] - ans1//2)
print(ans1, ans2)
