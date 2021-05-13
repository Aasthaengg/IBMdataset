N = int(input())
As = list(map(int,input().split()))
mi=0
ma=0
r = []
for i in range(N):
 rate = As[i]//400
 if rate < 8:
     if not rate in r:
         r.append(rate)
         mi += 1
         ma += 1
 else:
     ma+=1
if mi == 0:
    mi =1
print(mi,ma)