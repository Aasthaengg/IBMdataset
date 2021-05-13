n=int(input())
ab=[list(map(int,input().split()))for i in range(n)]
ab.sort(key=lambda x:x[0]+x[1],reverse=True)
b=[i[1]for i in ab]
s=[i[0]+i[1]for i in ab]
print(sum(s[::2])-sum(b))