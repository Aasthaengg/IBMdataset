def main():
    import sys
    sys.setrecursionlimit(311111)
    import numpy as np
    ikimasu = sys.stdin.buffer.readline
    ini = lambda: int(ins())
    ina = lambda: list(map(int, ikimasu().split()))
    ins = lambda: ikimasu().strip()
    n,k = ina()
    tmp = [[] for _ in range(n)]
    for _ in range(n-1):
        x,x1=  ina()
        x-=1
        x1-=1
        tmp[x].append(x1)
        tmp[x1].append(x)
    def dfs(teiru,ta):
        rick = 1
        coulduse = k-1 if ta==-1 else k-2
        for i in tmp[teiru]:
            if i == ta:
                continue
            rick*=coulduse
            rick%=1000000007
            coulduse-=1
            rick*=dfs(i,teiru) 
            rick%=1000000007
        return rick
    print(k*dfs(0,-1)%1000000007)
    

    


        
        
        


    
        


        


    




















if __name__ == "__main__":
    main()
