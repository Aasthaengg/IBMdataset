n,m = map(int,input().split())
s = input()
ans = []
now = n
while now>0:
    for i in range(m):
        if now-m+i>=0 and s[now-m+i]=='0':
            now = now-m+i
            ans.append(m-i)
            break
    else:
        print('-1')
        exit()
for i in ans[::-1]:
    print(i,end=' ')
