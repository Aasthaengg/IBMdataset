n = int(input())
a = list(map(int,input().split()))
a.append(0)
a = sorted(a)

while len(a) > 2:
    for i in range(2,n):
        a[i] %= a[1]
        
    a = sorted(set(a))
    n = len(a)
    
print(a[1])