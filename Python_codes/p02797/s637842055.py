n,k,s = map(int,input().split())
ans = []
kazu = 0

for i in range(n):
    if kazu != k:
        ans.append(s)
        kazu += 1
    else:
        if s == 1000000000:
            ans.append(1)
        else:
            ans.append(s+1)

for i in ans:
    print(i,end=' ')

print()
