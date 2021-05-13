N = int(input())
h = list(map(int,input().split()))
def g(ls):
    try:
        return ls.index(0)
    except:
        return -1
def f(ls):
    if ls==[]:
        return 0
    if len(ls) == 1:
        return ls[0]
    m = min(ls)
    ls = [x-m for x in ls]
    ans = m
    while ls:
        i = g(ls)
        if i == -1:
            ans += f(ls)
            break
        ans += f(ls[:i])
        ls = ls[i+1:]
    return ans
print(f(h))