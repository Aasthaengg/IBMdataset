n = int(input())

pf = {}


for i in range(2,int(n**0.5)+1):
    while n%i == 0:
        pf[i] = pf.get(i,0)+1
        n //= i
if n>1: pf[n] = 1

num_group = [0]*11 #2**50 > 10**12  55=1+2+...+10
for i in range(10):
    num_group[i+1] = num_group[i] + (i+1)
#print(num_group)

ans = 0
for prime in pf.keys():
    for i in range(1,11):
      if pf[prime]<num_group[i]:
          break
    ans += i-1
print(ans)