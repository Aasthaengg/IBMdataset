import math
def main():
    x = int(input())
    if(x>6):
        res = 1
    if(x%11<=6 and x%11!=0):
        a = math.ceil((x+5)/11)
        b = a-1
        print(a+b)
    else:
        a=math.ceil((x)/11)
        b=a
        print(a+a)
if __name__ == '__main__':
    main()
