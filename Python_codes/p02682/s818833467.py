import sys
input=sys.stdin.readline

def main():
    a,b,c,k = map(int, input().split())
    if a >= k:
        print(k)
    else: # aććå¤ć
        k -= a
        if b >= k:
            print(a)
        else:
            k -= b
            print(a-k)


if __name__=="__main__":
    main()
