import sys
import bisect as bi
import math
from collections import defaultdict as dd
import heapq
import itertools
input=sys.stdin.readline
##import numpy as np
#sys.setrecursionlimit(10**7)
mo=10**9+7
def cin():
    return map(int,sin().split())
def ain():            
    return list(map(int,sin().split()))
def sin():
    return input()
def inin():
    return int(input())
##def power(x, y):
##    if(y == 0):return 1
##    temp = power(x, int(y / 2))%mo
##    if (y % 2 == 0):return (temp * temp)%mo 
##    else:
##        if(y > 0):return (x * temp * temp)%mo 
##        else:return ((temp * temp)//x )%mo
##
##for _ in range(inin()):
r,c,k=cin()
dc=dd(int)
dr=dd(int)
mat=[]
for i in range(r):
    s=sin().strip()
    dr[i]=s.count('#')
    mat.append(list(s))
total=sum(list(dr.values()))
for i in range(c):
    co=0
    for j in range(r):
        if(mat[j][i]=='#'):
            co+=1
    dc[i]=co
ans=0
lr=lr=[o for o in range(r)]
lc=[o for o in range(c)]
for i in range(0,r+1):
    sur=0
    
##    print("LR==",lr)
    rowp=list(itertools.combinations(lr,i))
##    print("ROWPER==",rowp)
##    print(len(rowp))
    for perrow in rowp:
        sur=0
        for indexr in perrow:
            sur+=dr[indexr]
        for j in range(0,c+1):
            suc=0
            colp=list(itertools.combinations(lc,j))
            for percol in colp:
                suc=0
                for indexc in percol:
                    co=0
                    for ro in range(r):
                        if(mat[ro][indexc]=='#' and (ro not in perrow)):
                            co+=1
                    suc+=co
                if(total-sur-suc==k):
##                    print("No of ro=",i,"SUMR",sur,"ROWPERM=",perrow,"   ","NO OF COL",j,"SUMC",suc,"COLPERM",percol)
                    ans+=1
                        
                    
print(ans)
    
        
    

        


    


    
    
    
    
    
    
    
    
        
    
    
    
    
    
    
        
        
    
    
    
    


    





##
        
    
    
    
    
    
    
        
        
    
    
    
    


    





##def msb(n):n|=n>>1;n|=n>>2;n|=n>>4;n|=n>>8;n|=n>>16;n|=n>>32;n|=n>>64;return n-(n>>1) #2 ki power
##def pref(a,n,f):             
##    pre=[0]*n
##    if(f==0):         ##from beginning
##        pre[0]=a[0]
##        for i in range(1,n):
##            pre[i]=a[i]+pre[i-1]
##    else:              ##from end
##        pre[-1]=a[-1]
##        for i in range(n-2,-1,-1):
##            pre[i]=pre[i+1]+a[i]
##    return pre
##maxint=10**24 
##def kadane(a,size): 
##    max_so_far = -maxint - 1
##    max_ending_here = 0
##       
##    for i in range(0, size): 
##        max_ending_here = max_ending_here + a[i] 
##        if (max_so_far < max_ending_here): 
##            max_so_far = max_ending_here 
##  
##        if max_ending_here < 0: 
##            max_ending_here = 0   
##    return max_so_far
