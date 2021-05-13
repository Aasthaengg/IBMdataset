a1,a2,a3=map(int,input().split())
a=[abs(a1-a2),abs(a1-a3),abs(a2-a3)]
a.sort()
result=0
for i in range(2):
    result+=a[i]
print(result)