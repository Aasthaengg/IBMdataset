import sys
input = sys.stdin.readline
from itertools import product
INF = 10**9
MOD = 10**9 + 7

def main():
    n = int(input())
    a = list(map(int,input().split()))

    ans , right = 0 , 0 
    cnt_1 = [0] * 20
    power = [pow(2,i) for i in range(20)]
    keta = [[0]*20 for _ in range(n)]

    for left in range(n):
        flag = False
        while right < n:
            for i in range(20):
                if (a[right]>>i)&1:
                    cnt_1[i] += 1
                    keta[right][i] = 1
                    a[right] ^= power[i]
                if cnt_1[i] == 2:
                    flag = True
            
            if flag:
                break
            else:
                right += 1

        for i in range(20):
            if keta[left][i]:
                cnt_1[i] -= 1
        ans += right - left
        if right - left == 1:
            right += 1
    
    print(ans)
if __name__=='__main__':
    main()
