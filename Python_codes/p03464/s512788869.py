k = int(input())
a = list(map(int,input().split()))
ansmax = 2
ansmin = 2

for i in reversed(range(k)):
    if ansmax - ansmin < a[i] and (ansmin%a[i])*(ansmax%a[i]) != 0 and (ansmax%a[i]) >= (ansmin%a[i]):
        print(-1)
        exit()
    ansmin = -(-ansmin//a[i])*a[i]
    ansmax = (ansmax//a[i])*a[i] + a[i] - 1
print(str(ansmin) + " " + str(ansmax))
