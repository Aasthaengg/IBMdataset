n = int(input())
B = list(map(int,input().split()))

ans = []
while B:
    for i,v in enumerate(B[::-1]):
        if len(B)-i == v:
            a = B.pop(len(B)-i-1)
            ans.append(a)
            break
    else:
        break
if not B:
    print(*ans[::-1],sep='\n')
else:
    print(-1)