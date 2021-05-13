def main():
    s = int(input())
    N = 10**9

    y2 = 1
    y3 = s // N + 1
    x3 = N - s % N
    if y3 == N+1:
        y2 = 0
        y3 = N
        x3 = N
    
    print("0 0 1000000000 {} {} {}".format(str(y2),str(x3),str(y3))) 

if __name__ == '__main__':
    main()