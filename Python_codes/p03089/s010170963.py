N = int(input())
ans = []
b = list(map(int,input().split()))
while b:
    i = len(b)-1
    while b[i] != i+1 and i >= 1:
        i -= 1
    if b[i] == i+1:
        ans.append(b.pop(i))
    else:
        break
if b:
    print(-1)
else:
    for i in ans[::-1]:
        print(i)