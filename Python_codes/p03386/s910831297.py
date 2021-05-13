a, b, k = map(int, input().split())

ans = []
for i in range(a, a+k):
    if i not in ans and (a <= i and i <= b):
        ans.append(i)

for i in range(b-k+1, b+1):
    if i not in ans and (a <= i and i <= b):
        ans.append(i)
    
for i in range(len(ans)):
    print(ans[i])