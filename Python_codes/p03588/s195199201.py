n = int(input())
a = [0]*n
for i in range(n):
    a[i] = list(map(int,input().split()))
a.sort(key= lambda val : val[0],reverse=True)
print(a[0][0] + a[0][1])