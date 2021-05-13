def attack(x):
    if x==1:
        return 1
    else:
        return 2*attack(x//2)+1
h=int(input())
res=attack(h)
print(res)