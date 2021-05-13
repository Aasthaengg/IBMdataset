N = int(input())
B = list(map(int,input().split()))

for i,b in enumerate(B):
    if i + 1 < b:
        print(-1)
        exit()

N = len(B)
ans = []
for _ in range(N):
    for i,b in enumerate(B):
        if i+1 == b:
            t = i+1

    B.pop(t-1)
    ans.append(t)
for i in ans[::-1]:
    print(i)
