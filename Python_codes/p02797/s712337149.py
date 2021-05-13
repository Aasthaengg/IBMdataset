n,k,s = map(int,input().split())

ans = []

for i in range(k):
    ans.append(s)

for i in range(n-k):
    if s != 10**9:
        ans.append(10**9)
    else:
        ans.append(10**9-1)

ans1 = ""
for i in ans:
    ans1 += str(i)+ " "
print(ans1)