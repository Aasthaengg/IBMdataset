a = input()
n = len(a)

dic = {}
for i in range(n):
    if a[i] in dic:
        dic[a[i]] += 1
    else:
        dic[a[i]] = 1

ans = n*(n-1)//2
for i in dic.values():
    ans -= i*(i-1)//2
print(ans+1)