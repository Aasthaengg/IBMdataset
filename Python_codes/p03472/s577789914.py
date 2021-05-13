n,h = map(int,input().split())
a = []
b = []

for i in range(n):
    a_,b_ = map(int,input().split())
    a.append(a_)
    b.append(b_)
b.sort(reverse = True)
max_a = max(a)
ans =0

for i in range(n):
    ans +=1
    if max_a > b[i]:
        ans -=1
        break
    h -= b[i]
    if h <= 0:
        break
    
if h > 0: 
    d,f = divmod(h,max_a)
    ans += d
    if f != 0:
        ans +=1
print(ans)