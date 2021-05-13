import sys
stdin = sys.stdin

sys.setrecursionlimit(10**5)

def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x)-1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

def get_init(n: int):
    left = 0
    right = n-1
    dic = {}
    
    
    print(left, flush=True)
    s = ns()
    if s == 'Vacant':
        exit()
    elif s == 'Male':
        dic.update({0: 'Male'})
    else:
        dic.update({0: 'Female'})
        
        
    print(right, flush=True)
    s = ns()
    if s == 'Vacant':
        exit()
    elif s == 'Male':
        dic.update({1: 'Male'})
    else:
        dic.update({1: 'Female'})
        
    return dic

def search(n:int, dic: dict):
    left = 0
    right = n-1
    
    while right-left > 1:
        middle = (right+left)//2
        print(middle, flush=True)
        s = ns()
        if s == 'Vacant':
            exit()
        elif s == dic[middle%2]:
            left = middle
        else:
            right = middle
            
    print(left, flush=True)
    s = ns()
    if s == 'Vacant':
        exit()
        
    print(right, flush=True)
    s = ns()
    if s == 'Vacant':
        exit()
            

n = ni()

dic = get_init(n)
search(n, dic)