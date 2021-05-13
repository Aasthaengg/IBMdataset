n = int(input())
b = list(map(int, input().split()))

ans = []
l = len(b)
while l > 0:
    for i in range(l):
        ii = l - i
        if b[ii-1] == ii:
            ans.append(ii)
            del b[ii-1]
            l = l - 1
            break
    else:
        print(-1)
        exit(0)

for a in ans[::-1]:
    print(a)
