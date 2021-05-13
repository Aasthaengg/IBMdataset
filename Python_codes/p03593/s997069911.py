import sys
#input = sys.stdin.buffer.readline
from collections import defaultdict

def main():
    H,W = map(int,input().split())
    d = defaultdict(int)
    for _ in range(H):
        s = input()
        for st in s:
            num = ord(st)-ord("a")
            d[num] += 1
    
    use = list(d.values())
    m = [0,0,0]
    for num in use:
        m[0] += num//4
        num -= num//4*4
        m[1] += num//2
        m[2] += num%2

    if (H%2 == 0 and W%2 == 0):
        if H*W == 4*m[0]:
            print("Yes")
        else:
            print("No")
    elif (H*W)%2 == 1:
        if m[2] != 1:
            print("No")
        else:
            if m[0] >= ((H-1)*(W-1))//4:
                print("Yes")
            else:
                print("No")
    else:
        if m[2] != 0:
            print("No")
        else:
            if H%2 == 1:
                if m[1] <= W//2:
                    print("Yes")
                else:
                    print("No")
            else:
                if m[1] <= H//2:
                    print("Yes")
                else:
                    print("No")

if __name__ == "__main__":
    main()
