n = int(input())
a = list(map(int, input().split()))

sita_maxi = [0 for i in range(n+1)]
sita_maxi[n] = a[n]
for i in range(n-1, -1, -1):
    sita_maxi[i] = sita_maxi[i+1] + a[i]

if a[0] > 1:
    print(-1)
    exit()

lst = [1]
for i in range(1, n+1):
    lst.append(min((lst[i-1]-a[i-1])*2, sita_maxi[i]))
    if lst[-1] < a[i]:
        print(-1)
        exit()

print(sum(lst))
