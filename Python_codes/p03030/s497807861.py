n = int(input())
a = []
for i in range(n):
    s, p = input().split()
    p = int(p)*-1
    a.append([i+1,s,p])
a = sorted(a, key=lambda x:(x[1], x[2]))
for i in range(n):
    print(a[i][0])