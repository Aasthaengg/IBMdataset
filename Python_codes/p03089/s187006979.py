n=int(input())
b = list(map(int, input().split()))
ans=[]
for num in range(n):
    dl=-1
    for i in range(len(b)):
        if b[i] == i+1:
            dl=i
    if dl==-1:
        print(-1)
        exit()
    b.pop(dl)
    ans.append(dl+1)
ans = list(reversed(ans))
for i in ans:
    print(i)