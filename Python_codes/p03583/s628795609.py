import sys
input = sys.stdin.buffer.readline

def main():
    N = int(input())
    if N%2 == 0:
        print(N,N,N//2)
    else:
        x,y,z = 0,0,0
        for h in range(1,3501):
            for k in range(h,3501):
                if ((4*h*k-N*(h+k))>0 and (N*h*k)%(4*h*k-N*(h+k)) == 0):
                    x = h
                    y = k
                    z = (N*h*k)//(4*h*k-N*(h+k))
                    break
            if z != 0:
                break
        print(x,y,z)

if __name__ == "__main__":
    main()
