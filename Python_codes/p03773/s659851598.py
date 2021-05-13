import itertools,collections
def main():
    a,b=map(int, input().split())
    if(a+b>23):
        print(abs(24-(a+b)))
    else:
        print(a+b)

if __name__ == '__main__':
    main()
