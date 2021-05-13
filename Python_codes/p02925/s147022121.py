import sys
input = sys.stdin.readline

from collections import deque

def main():

    n = int(input())
    
    a = [[int(i) for i in input().split()] for j in range(n)]
    
    check = [0]*n
    used = [0]*n
    
    d = deque()
    
    for i in range(n):
        if used[i] == 1:
            continue
        ai = a[i][0]-1
        if a[ai][0] == i+1:
            d.append([i+1,ai+1])
            used[i] = 1
            used[ai] = 1
            check[i] = 1
            check[ai] = 1
            
    ans = 0
    
    if len(d) == 0:
        print(-1)
        exit()
    
    #print(d)
    
    while len(d) > 0:
        used = [0]*n
        ans += 1
        num = len(d)
        for i in range(num):
            tmp = d.popleft()
            for j in range(2):
                mys = tmp[j]-1
                if check[mys] != n-1 and used[mys] == 0:
                    psn = a[mys][check[mys]]-1
                    if check[psn] != n-1 and used[psn] == 0:
                    #print(tmp,psn,a[psn][check[psn]])
                    #print(i,j,tmp,psn,check[mys],check[psn])
        
                        if a[psn][check[psn]] == mys+1:
                            d.append([psn+1,mys+1])
                            used[mys] = 1
                            used[psn] = 1
                            check[mys] += 1
                            check[psn] += 1
        #print(d)
        
    for i in range(n):
        if check[i] != n-1:
            print(-1)
            exit()
    
    print(ans)

if __name__ == '__main__':
    main()