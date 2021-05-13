N = 0;
i = 0;
tmp = 0;
ans = 0;

N = int(input());

for i in range(1,10,1):
    if N%i!=0:
        continue;
    tmp = N/i;
    
    if tmp<=9 and tmp>=1:
        ans+=1;

if ans>0:
    print('Yes');
    
else:
    print('No');

