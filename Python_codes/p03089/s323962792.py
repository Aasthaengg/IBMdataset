N = int(input())
B = list(map(lambda x: int(x)-1, input().split()))

ans = []
for i in range(N):
    erase = -1
    for c in reversed(range(len(B))):
        if B[c] == c:
            erase = c
            break
    
    if erase == -1:
        print(-1)
        exit()
    else:
        ans.append(erase)
        B.pop(erase)

for _ in ans[::-1]:
    print(_+1)