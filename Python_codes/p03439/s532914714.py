import sys
input = sys.stdin.buffer.readline

def main():
    N = int(input())
    left = 0
    right = N
    print(left,flush=True)
    ls = input()
    if ls == "Vacant":
        exit()
        
    while right-left > 1:
        mid = (right+left)//2
        print(mid,flush=True)
        nls = input()
        if nls == "Vacant":
            exit()
        if nls == ls:
            if (mid-left)%2 == 0:
                left = mid
            else:
                right = mid
        else:
            if (mid-left)%2 == 1:
                left = mid
                ls = nls
            else:
                right = mid

if __name__ == "__main__":
    main()
