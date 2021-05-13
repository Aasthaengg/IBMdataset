n = int(input())
mod0 = set()
mod1 = set()

for i in range(1, int(n**0.5)+1):
    if n%i==0:
        mod0.add(i)
        mod0.add(n//i)
    if (n-1)%i==0:
        mod1.add(i)
        mod1.add((n-1)//i)
mod0.remove(1)
mod1.remove(1)
ans = 0
for i in mod0:
    nn = n
    while nn%i==0:
        nn//=i
    if nn%i==1:
        ans += 1
ans += len(mod1)
print(ans)