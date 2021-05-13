n,k = map(int,input().split())
li = list(map(int,input().split()))
t = list(input())
ans = []
for i in range(len(t)):
    if t[i] == 'r':
        if k <= i and t[i] == t[i-k]:
            t[i] = ''
            ans.append(0)
        else:
            ans.append(li[2])
    elif t[i] == 's':
        if k <= i and t[i] == t[i-k]:
            t[i] = ''
            ans.append(0)
        else:
            ans.append(li[0])
    else:
        if k <= i and t[i] == t[i-k]:
            t[i] = ''
            ans.append(0)
        else:
            ans.append(li[1])
print(sum(ans))