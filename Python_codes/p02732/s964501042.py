n = int(input())
a = list(map(int,input().split()))

a_2 = [0 for i in range(n)]
for i in range(n):
    a_2[a[i]-1] += 1

al = [0 for i in range(n)]
c = 0
for i in a_2:
    if i > 1:
        al[c] += i * (i-1) / 2
    c += 1

sine = sum(al)
for i in range(n):
    f = a[i]
    t = a_2[f-1] - 1
    print(int(sine-(al[f-1]-t*(t-1)/2)))
    
