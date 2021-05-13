# -*- coding: utf-8 -*-
def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(int(input()))
    now = 1
    check = [0]*N
    ans = 0
    # while(1):
    for k in range(N):
        if now == 2:
            print(ans)
            return
        # if check[now-1] == 1:
        #     print(-1)
        #     return
        else:
            check[now-1] = 1
        now = A[now-1]
        ans += 1
        # print(now)
    print(-1)
    return
        
        
if __name__ == '__main__':
    main()