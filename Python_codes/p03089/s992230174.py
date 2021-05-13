N = int(input())
*l, = map(int, input().split())

ans = []
for _ in range(N):
    for i in range(len(l))[::-1]:
        if l[i]==(i+1):
            ans.append(l[i])
            del l[i]
            break
        
if l:
    print(-1)
else:
    for i in ans[::-1]:
        print(i)
