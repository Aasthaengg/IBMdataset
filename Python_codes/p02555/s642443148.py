s = int(input())
a = 10**9+7
l = [1]+[0]*s
for i in range(3,s+1):
    l[i] = l[i-3]+l[i-1]
print(l[s]%a)