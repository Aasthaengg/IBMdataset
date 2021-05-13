n = int(input())
a = list(map(int, input().split()))

ar = list(reversed(a))
#print(ar)
com = [ar[0]]
for i in range(n):
    com.append(com[i] + ar[i+1])
#print(com)
com.reverse()
ans = 0
val = 1
for i in range(n+1):

    ans += min(val,com[i])
    val -= a[i]
    if (i < n and val <= 0) or (i == n and val < 0) or (i == n and a[i] == 0):
        print(-1)
        exit()
    val *= 2
print(ans)
