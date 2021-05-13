def main():
    import sys
    ikimasu = sys.stdin.buffer.readline
    ini = lambda: int(ins())
    ina = lambda: list(map(int, ikimasu().split()))
    ins = lambda: ikimasu().strip()
    
    n = ini()
    rick = 0
    import math
    for i in range(1,n+1):
        rick+=math.floor((n-1)/i)
    print(rick)
        


    
        


        


    




















if __name__ == "__main__":
    main()