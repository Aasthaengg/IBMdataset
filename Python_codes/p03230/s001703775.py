n = int(input())
t = 2*n
a = int(t**0.5)
if a*(a+1) != t:
    print("No")
    exit()

print("Yes")
print(a+1)
count = [0]*n
ans = [[] for i in range(a+1)]
now = a
p = [0]*(a+1)
for i in range(a):
    ans[i].append(i+1)
    ans[i+1].append(i+1)
    count[i] += 2
for i in range(a+1):
    if i >= 2:
        for j in range(i-1):
            while count[ans[j][p[j]]-1] ==2:
                p[j] += 1
            x = ans[j][p[j]]
            ans[i].append(x)
            count[x-1] +=1
        x = len(ans[i])
        for j in range(a-x):
            ans[i].append(now+1)
            count[now]+=1
            now += 1
    else:
        x = len(ans[i])
        for j in range(a-x):
            ans[i].append(now+1)
            count[now]+=1
            now += 1
    
for i in range(a+1):
    print(a,*ans[i])
