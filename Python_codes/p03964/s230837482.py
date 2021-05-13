n = int(input())

t = [0 for i in range(n)]
a = [0 for i in range(n)]

for i in range(n):
    t[i],a[i] = map(int,input().split())

t_num = t[0]
a_num = a[0]

for i in range(1,n):
    k = max(-(-t_num//t[i]),-(-a_num//a[i]))
    #その比に票を合わせる
    t_num,a_num = k*t[i],k*a[i]

print(t_num + a_num)
