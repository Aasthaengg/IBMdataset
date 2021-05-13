n = int(input())
a = list(map(int,input().split()))
dic = {}
for i in range(n):
    dic.setdefault(a[i],i+1)
ans = []
for i in range(1,n+1):
    print(str(dic[i]),end='')
    print(' ',end='')
