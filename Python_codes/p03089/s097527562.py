from fractions import gcd

def mi():
    return map(int, input().split())

def main():
    N = int(input())
    b = list(mi())
    a = []
    for i in range(N):
        bl = False
        for j, v in enumerate(b):
            if v == j+1:
                t = j
                bl = True
        if bl:
            a.append(b.pop(t))
        else:
            print(-1)
            return
    
    for v in reversed(a):
        print(v)



if __name__ == '__main__':
    main()