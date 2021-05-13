n = int(input())
l = list(map(int, input().split()))

for i in range(n):
    if l[i] > i+1:
        print(-1)
        exit()

ans = []
while len(l) > 0:
    for i, x in enumerate(l[::-1]):
        if len(l) - i == x:
            ans.append(x)
            l.pop(len(l)-i-1)
            break
for i, x in enumerate(ans[::-1]):
    print(x)

