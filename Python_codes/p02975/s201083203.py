n = int(input())
lst = list(map(int,input().split()))
l_unique = sorted(list(set(lst)))

flg = False
if len(l_unique)==1:
    x = l_unique[0]
    if x==0:
        flg = True
elif len(l_unique) == 2:
    x,y = l_unique[0], l_unique[1]
    if x==0 and n%3==0:
        num = n//3
        if lst.count(x)==num and lst.count(y)==2*num:
            flg = True
elif len(l_unique) == 3:
    x,y,z = l_unique[0], l_unique[1], l_unique[2]
    if n%3 == 0:
        num = n//3
        if lst.count(x)==num and lst.count(y)==num and lst.count(z)==num:
            if (x^y^z)==0:
                flg = True
print('Yes' if flg else 'No')