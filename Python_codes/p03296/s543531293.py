N = int(input())
a = list(map(int, input().split()))

ans = []
count = 0
for i in range(0,N):
    if i == 0:
        count = 1
    elif i == N-1:
        if a[i] == a[i-1]:
            count += 1
            ans.append(count)
        else:
            ans.append(count)
            count = 1
            ans.append(count)
    else:
        if a[i] == a[i-1]:
            count += 1
        else:
            ans.append(count)
            count = 1
        
an = 0
for i in range(len(ans)):
    an += ans[i]//2

print(an)