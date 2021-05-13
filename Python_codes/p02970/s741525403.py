import math
def main():
    n,d=map(int, input().split())
    #一人当たり2*d+1
    print(math.ceil((n)/(2*d+1)))

if __name__ == '__main__':
    main()
