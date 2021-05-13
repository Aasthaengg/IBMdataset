#coding:utf-8
def jyu_waru(a):
    x = a
    b = 0
    while x>10:
        x = x//10
        if x%10 ==3:
            b = a
            break
    return b

n = int(input().rstrip())
kazu =[]
x = 0
for i in range(1,n+1):
    if i%3==0:
        kazu.append(i)
        
    elif i%10 ==3:
        kazu.append(i)

    else:
        x = jyu_waru(i)
        if x != 0:
            kazu.append(i)

print(" " +" ".join(list(map(str,kazu))))