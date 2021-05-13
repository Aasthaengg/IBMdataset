n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
un = 0
ov = []
ans = 0
for i in range(n):
    if a[i] < b[i]:
        un += b[i] - a[i]
        ans += 1
    elif a[i] > b[i]:
        ov.append(a[i] - b[i])
if un == 0:
    print(0)
    exit()
ov.sort(reverse = True)
for i in ov:
    un -= i
    ans += 1
    if un <= 0:
        print(ans)
        exit()
print(-1)