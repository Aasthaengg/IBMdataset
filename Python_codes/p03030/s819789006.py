n = int(input())
a = [[input().split(),i + 1] for i in range(n)]
a = sorted(a,key = lambda x:(x[0][0],-int(x[0][1])))

for j in range(n):
    print(a[j][1])