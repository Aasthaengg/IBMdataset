from sys import stdin,setrecursionlimit
setrecursionlimit(10**6)
def S(): return stdin.readline().rstrip()

def f(ls,stock,save):
    if len(ls)<1:
        return int(stock)+save
    else:
        stock += ls.pop(0)
        sum = 0    
        if 0<len(ls):
            buff = ls[:]
            sum += f(buff,'0',save+int(stock))
        buff = ls[:]
        sum += f(buff,stock,save)
        return sum

s = S()
ls = list(s)
ans = f(ls,'0',0)
print(ans)