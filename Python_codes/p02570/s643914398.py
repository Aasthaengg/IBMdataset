def fun(ls):
    a,b,c = ls
    if b*c>=a:
        print('Yes')
    else:
        print('No')


T = list(map(int, input().split()))
fun(T)