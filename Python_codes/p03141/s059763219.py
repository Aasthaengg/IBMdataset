import sys
input= lambda: sys.stdin.readline().rstrip()
def pin(type=int):return map(type,input().split())
def tup(t=int):return tuple(pin(t))
#%%code
def resolve():
    N=int(input())
    AB=[tup()for i in range(N)]
    AB.sort(key=lambda x:sum(x),reverse=True)
    #print(AB)

    n=N
    turn=0
    his=0
    her=0
    for i in range(N):
        if i%2==0:
            his+=AB[i][0]
        else:her+=AB[i][1]
    print((his-her))
            
#%%submit!
resolve()