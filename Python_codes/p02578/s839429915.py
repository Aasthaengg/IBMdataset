N = int(input())
str_in = input()
num = [int(n) for n in str_in.split()]
num = list(map(int, str_in.strip().split()))

hight = num[0]
stools = 0

for x in range(1,len(num)):
    if hight>num[x]:
        stools+=hight-num[x]
    elif num[x] > hight:
        hight = num[x]       
print (stools)