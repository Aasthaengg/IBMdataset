
        
def main():
    import sys
    def input(): return sys.stdin.readline().rstrip()

    n = int(input())
    flag = 0
    for i in range(n):
        a = int(input())
        if a%2 == 1:
            print('first')
            return
    print('second')


    




                
if __name__ == '__main__':
    main()