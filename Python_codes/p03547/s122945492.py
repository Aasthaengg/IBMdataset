import collections
def main():
    x,y=map(str, input().split())
    if(x>y):
        print(">")
    elif(y>x):
        print("<")
    else:
        print("=")

if __name__ == '__main__':
    main()
