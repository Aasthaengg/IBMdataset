n = int(input())
s = list(map(str,input().split()))
dic = {}
for i in range(n):
    dic.setdefault(s[i],0)
    dic[s[i]] += 1
#print(len(dic))
if len(dic)==4:
    print('Four')
else:
    print('Three')