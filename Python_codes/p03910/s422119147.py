import sys
input= lambda: sys.stdin.readline().rstrip()
#cythonを使うために実行
#%load_ext Cython
#%%code
def resolve():
    N=int(input())
    ans=0
    for i in range(1,N*2):
        ans+=i
        if ans >= N:
            stop=i+1
            j=ans-N
            break
    for k in range(1,stop):
        if k!=j:print(k)
        
#%%submit!
resolve()
