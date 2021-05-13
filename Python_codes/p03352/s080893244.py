A = int(input())
ans = []
for i in range(1,32):
    for j in range(2,1000):
        ans.append(i ** j)
ans.sort()
for h in range(len(ans)):
    if A < ans[h]:
        print(ans[h - 1])
        exit()