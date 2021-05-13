N = int(input())
blist = list(map(int, input().split()))
ans = []
for i in range(N):
    for index in range(N-i-1, -1, -1):
        if blist[index] == index + 1:
            ans.append(blist.pop(index))
            break
    else:
        print(-1)
        break
else:
    for num in ans[::-1]:
        print(num)
