
        
def main():
    import sys
    def input(): return sys.stdin.readline().rstrip()

    n = int(input())
    for i in range(1, 3501):
        for j in range(i, 3501):
            mod = 4*i*j - n*(i+j)
            if mod > 0 and (n*i*j)%mod == 0:
                k = (n*i*j)//mod
                print(i, j, k)
                exit(0)
    




                
if __name__ == '__main__':
    main()