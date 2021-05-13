n = int(input())
B = list(map(lambda x: x-1, map(int, input().split())))
ans = []
for i in range(n):
    for j in range(len(B)-1,-1,-1):
        if B[j]==j:
            ans.append(j+1)
            del B[j]
            break
        elif j==0:
            ans = -1
            break
    if ans==-1:
        break

if ans == -1:
    print(ans)
else:
    for _ans in ans[::-1]:
        print(_ans)