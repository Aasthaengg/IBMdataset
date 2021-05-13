import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

"""
k組ある，
ある組から見て，残りの(k-1)組と被りが1つずつあるから要素数はk-1

"""

def main():
    mod=10**9+7
    N=I()

    k=0
    for i in range(N+5):
        ii=i*(i-1)
        if ii==2*N:
            k=i
            break
    if k==0:
        print("No")
        exit()
    
    ans=[[]for _ in range(k)]
    now=1#配る数字
    import itertools
    
    for ite in itertools.combinations(range(k),2):
        i=ite[0]
        j=ite[1]
        ans[i].append(now)
        ans[j].append(now)
        now+=1
        
    print("Yes")
    print(k)
    for i in range(k):
        print(len(ans[i]),' '.join(map(str, ans[i])))
        
        
            
            
            
 
        

main()
