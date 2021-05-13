N = int(input())
b = list(map(int,input().split()))

ans = []
while len(b):
    memo = -1
    for key,val in enumerate(b):
        if key+1==val:
            memo = key
    if memo != -1:
        ans.append(b.pop(memo))
    else:
        break

if len(b):
    print(-1)
else:
    ans.reverse()
    for a in ans:
        print(a)