n = int(input())
a,b = map(int,input().split())
p_list = list(map(int,input().split()))
p_list.sort()
ans = 0
dum1 = 0
dum2 = 0
dum3 = 0
for i in p_list:
    if i <= a:
        dum1 += 1
    if a+1 <= i <= b:
        dum2 += 1
    if i >= b+1:
        dum3 += 1
print(min(dum1,dum2,dum3))