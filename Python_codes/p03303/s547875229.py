def ip():
    return int(input())
    
def ipp():
    return map(int,input().split())
    
def sar():
    return list(ipp())
    
def pars(a):
    print(''.join(list(map(str, a))))
    print('\r')
    
def parl(a):
    print('\r'.join(list(map(str, a))))
    print('\r')
    
#template ends   

if __name__=='__main__':
    T=1
    #T=int(input().strip())
    for _ in range(T):
        s = input()
        k = ip()
        for i in range(0,len(s),k):
            print(s[i], end="")