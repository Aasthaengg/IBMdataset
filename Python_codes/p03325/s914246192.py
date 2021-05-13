def chk(n):
    global dic
    cnt = 0
    while n%2==0:
        n = n//2
        cnt += 1
    dic.setdefault(cnt,0)
    dic[cnt] += 1
    return cnt

dic = {}
dic.setdefault(0,0)
n = int(input())
a = list(map(int,input().split()))
for i in range(n):
    tmp = chk(a[i])
#print(dic)
ans = 0
for item in dic.items():
    ans += item[0]*item[1]
print(ans)