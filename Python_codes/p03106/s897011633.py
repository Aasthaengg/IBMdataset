
a , b , k = map(int,input().split())
cou = 0
for i in reversed(range(1,101)):
    if a % i == 0 and b % i == 0:
        cou += 1
    if cou == k:
        print(i)
        exit()