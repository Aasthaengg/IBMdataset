import heapq
from math import ceil

def check(ls,mid,a,b):
    count = 0
    for now in ls:
        now -= mid*b
        count += ceil(max(now,0)/(a-b))
    if count<=mid:
        return True
    else:
        return False

def main():
    n,a,b = map(int,input().split())
    h = [int(input()) for _ in range(n)]
    can_l,can_r = 0,10**9
    while 1:
        if can_r==can_l:
            print(can_r)
            exit()
        elif abs(can_r-can_l)==1:
            if check(h,max(can_r,can_l),a,b):
                print(max(can_l,can_r))
                exit()
            else:
                print(min(can_l,can_r))
                exit()
        mid = ceil((can_l+can_r)/2)
        if check(h,mid,a,b):
            can_r = mid
        else:
            can_l = mid
        
if __name__ == "__main__":
    main()