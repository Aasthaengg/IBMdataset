import math
import numpy as np
def main():
    mod = 1000000007
    N = int(input())
    mp = {}
    zero = 0
    for _ in range(N):
        x , y = map(int, input().split())
        if x == 0 and y == 0:
            zero += 1
        else:
            g = math.gcd(x, y)
            x //= g
            y //= g
            rot = 0
            if x == 0:
                y = 1
            else:
                if y == 0:
                    rot = 1
                    x = 0
                    y = 1
                else:
                    if x < 0 and y < 0:
                        x *= -1
                        y *= -1
                    elif x < 0:
                        rot = 1
                        x *= -1
                        x, y = y, x
                    elif y < 0:
                        rot = 1
                        y *= -1
                        x, y = y, x
            if (x, y) not in mp.keys():
                mp[x, y] = [0, 0]
                mp[x, y][rot] = 1
            else:
                mp[x, y][rot] += 1
        #print(mp)    
    #print(mp)
    ans = 1
    for (a, b) in mp.keys():
        now = 1
        #now += np.power(2, mp[a, b][0]) -1 
        #now += np.power(2, mp[a, b][1]) -1
        now += pow(2, mp[a, b][0], mod) -1 
        now += pow(2, mp[a, b][1], mod) -1
        ans *= now % mod
    ans += zero - 1
    print(ans % mod)
            
if __name__ == '__main__':
    main()