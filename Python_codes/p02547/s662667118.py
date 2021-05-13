def LI():
    return list(map(int, input().split()))


N = int(input())
count = 0
ans = "No"
for i in range(N):
    a, b = LI()
    if a == b:
        count += 1
        if count == 3:
            ans = "Yes"
            break
    else:
        count = 0
print(ans)
