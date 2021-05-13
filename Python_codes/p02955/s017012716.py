n, k = map(int, input().split( ))
a = list(map(int, input().split( )))

a_sum = sum(a)

rt_sm = int(a_sum**(1/2) + 0.01)

fct = []
fct2 = []

for p in range(1,rt_sm+1):
    if a_sum%p == 0:
        fct.append(p)
        fct2.append(a_sum//p)

if fct[-1] == fct2[-1]:
    fct.pop() 

fct += fct2
fct.sort(reverse=True)


for f in fct:
    tmp = []
    for t in a:
        tmp.append(t%f)
    tmp_sum = sum(tmp)
    cnt = 0

    sb = tmp_sum // f
    tmp.sort()
    for i in range(n-sb,n):
        tmp[i] -= f

    if sum(tmp[:n-sb]) <= k:
        ans = f 
        break

print(ans)
    
