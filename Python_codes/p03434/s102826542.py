n = int(input())
alst = list(map(int, input().split()))
alst.sort(reverse = True)
ans = 0
pm = 1
for a in alst:
    ans += a * pm
    pm *= -1
print(ans)