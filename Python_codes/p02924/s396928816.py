def main():
    import sys

    def input(): return sys.stdin.readline().rstrip()
    
    n = int(input())
    print((n-1)*n//2)




if __name__ == '__main__':
    main()