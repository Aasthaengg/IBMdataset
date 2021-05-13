from collections import Counter
a = input()
n = len(a)
data = Counter(a)
#print(data)
ans = n*(n-1)//2 + 1
for i in data:
    ans -= (data[i]-1)*data[i]//2

print(ans)