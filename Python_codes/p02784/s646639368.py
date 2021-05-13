#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))

h,n = map(int, input().split())
a = list(map(int, input().split()))

ans = 'No'
total = 0
for i in range(n):
    total += a[i]
    if total >= h:
        ans = 'Yes'
        break
print(ans)


