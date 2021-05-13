n = int(input())
l = list(map(int,input().split()))

if n == 1:
    l = list(map(str,l))
    print(" ".join(l))
    exit()

ans = []

if n%2 == 0:
    tmp = n
    for j in range(n//2-1):
        ans.append(tmp)
        tmp -= 2
    ans.append(tmp)
    ans.append(1)
    tmp = 1
    for j in range(n//2-1):
        tmp += 2
        ans.append(tmp)
else:
    tmp = n
    for j in range(n//2):
        ans.append(tmp)
        tmp -= 2
    ans.append(tmp)
    tmp = 2
    for j in range(n//2):
        ans.append(tmp)
        tmp += 2

ans2 = [0]*n
cnt = 0
for i in ans:
    ans2[cnt] = str(l[i-1])
    cnt += 1


print(" ".join(ans2))
