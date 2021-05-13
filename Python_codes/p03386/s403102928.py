a, b, k=map(int, input().split())

ans=[]
for i in range(k):
    if a+i not in ans and a+i<=b:
        ans.append(a+i)

for j in range(k):
    if b-j not in ans and b-j>=a:
        ans.append(b-j)

ans.sort()
for num in ans:
    print(num)
