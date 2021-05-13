n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))


a.sort()
b.sort()
c.sort()

ans = 0
j = 0
k = 0


for i in range(n):
    if j<n:
        while a[j]<b[i]:
            j+=1
            if j==n:
                break
    if k<n:
        while c[k]<=b[i]:
            k+=1
            if k==n:
                break

    ans += j*(n-k)


print(ans)