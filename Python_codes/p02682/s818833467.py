import sys
input=sys.stdin.readline

def main():
    a,b,c,k = map(int, input().split())
    if a >= k:
        print(k)
    else: # aより多い
        k -= a
        if b >= k:
            print(a)
        else:
            k -= b
            print(a-k)


if __name__=="__main__":
    main()
