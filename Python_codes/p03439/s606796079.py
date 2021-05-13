MOD = 10 ** 9 + 7
INF = 10 ** 10
import sys
sys.setrecursionlimit(100000000)
dy = (-1,0,1,0)
dx = (0,1,0,-1)

def main():
    n = int(input())
    a = [-1] * n
    print(0,flush = True)
    s = input()
    if s == 'Vacant':
        return
    elif s == 'Male':
        a[0] = 0
    else:
        a[0] = 1
    
    l = 0
    r = n
    for _ in range(19):
        mid = (r + l)//2
        print(mid,flush = True)
        s = input()
        if s == 'Vacant':
            return
        elif s == 'Male':
            a[mid] = 0
            if a[l] == 0:
                if (mid - l)%2 == 0:
                    l = mid
                else:
                    r = mid
            else:
                if (mid - l)%2 == 1:
                    l = mid
                else:
                    r = mid
        else:
            a[mid] = 1
            if a[l] == 0:
                if (mid - l)%2 == 1:
                    l = mid
                else:
                    r = mid
            else:
                if (mid - l)%2 == 0:
                    l = mid
                else:
                    r = mid
            
    return

if __name__ =='__main__':
    main()  