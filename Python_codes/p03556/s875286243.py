li =[]
for i in range(1000000):
    li.append(i**2)
N = int(input())
ans = []
for i in range(1000000):
    if li[i]<=N:
        ans.append(li[i])
print(max(ans))