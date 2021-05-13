def main():
    import sys
    ikimasu = sys.stdin.buffer.readline
    ini = lambda: int(ins())
    ina = lambda: list(map(int, ikimasu().split()))
    ins = lambda: ikimasu().strip()
    
    n= ini()
    tmp = 0
    for _ in range(n):
        l,r = ina()
        if(l==r):
            tmp+=1
            if(tmp==3):
                print("Yes")
                return
        else:
            tmp =0
    print("No")
        


        


    




















if __name__ == "__main__":
    main()