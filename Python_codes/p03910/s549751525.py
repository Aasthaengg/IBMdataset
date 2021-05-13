import sys
input= lambda: sys.stdin.readline().rstrip()
def pin(type=int):
    return map(type,input().split())

#%%code
def resolve():
    x=int(input())
    i=0;temp=0 
    while (1):
        i+=1
        temp+=i
        if temp > x:
            z=-x+temp
            
            for i in range(i):
                if i+1!=z:print(i+1)
            break
        if temp==x:
            for i in range(i):print(i+1)
            break
#%%submit!
resolve()