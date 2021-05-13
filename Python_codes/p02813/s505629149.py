import math
n = int(input())
def pos_num(l):
    l_sort = l.copy()
    l_len = len(l)
    l_sort.sort()
    if l_len == 1:
        an = 0
    else:
        #print(l_sort.index(l[0])+1)
        an = (l_sort.index(l[0]))*math.factorial(l_len-1)
    #print(an)
    return an 

    

ls = list(map(int, input().split()))
an = 0
for i in range(n-1):
    b = pos_num(ls[i:])
    an += b
    #print(an)
    

ll = list(map(int, input().split()))
bn = 0
for i in range(n-1):
    b = pos_num(ll[i:])
    bn += b
    #print(bn)

print(abs(an-bn))