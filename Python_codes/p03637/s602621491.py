#069_C
n = int(input())
a = list(map(int, input().split()))

mod1, mod2, mod4 = [0] * 3
for ai in a:
    if ai % 4 == 0:
        mod4 += 1
    elif ai % 2 == 0:
        mod2 +=1
    else:
        mod1 +=1
        
if mod2 == 0:
    print('No' if mod1 > mod4 + 1 else 'Yes')
else:
    print('No' if mod1 > mod4 else 'Yes')