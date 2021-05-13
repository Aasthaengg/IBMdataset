import sys
# import io, os
# input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
def main():
    n = int(input())
    a = sorted(list(map(int,input().split())))
    t = 10**10
    if a[-1]%2 == 0:
        for e in a:
            if abs(e-a[-1]//2) < abs(t-a[-1]//2):
                t = e
    else:
        for e in a:
            if abs(e-(1+a[-1])//2) < abs(t-(1+a[-1])//2):
                t = e
    print(a[-1],t)
if __name__ == '__main__':
    main()
