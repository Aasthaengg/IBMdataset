n = int(input())
t = []
a = []
for i in range(n):
    t_i, a_i = map(int, input().split())
    t.append(t_i)
    a.append(a_i)

vt = t[0]
va = a[0]

for i in range(n):
    if (vt * a[i] == va * t[i]):
        continue
    
    if(vt * a[i] < va * t[i]):
        x = (va + a[i] - 1)//a[i]
    elif (vt * a[i] > va * t[i]):
        x = (vt + t[i] - 1)//t[i]
    vt = x * t[i]
    va = x * a[i]

ans = vt + va
print(ans)