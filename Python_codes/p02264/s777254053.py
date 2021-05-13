n,q = list(map(int, input().split()))
p = [0]*n
t = [0]*n

for i in range(n):
    p[i],t[i] = list(input().split())

i = 0
sum_t = 0
while 1:
    if i==len(t):
        break
    tmp_t = int(t[i])-q
    if tmp_t<=0:
        sum_t += int(t[i])
        print(p[i],sum_t)
    else:
        sum_t += q
        p.append(p[i])
        t.append(tmp_t)        
    i+=1
