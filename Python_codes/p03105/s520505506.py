def main():
    #n = int(input())
    a,b,c = map( int, input().split())

    if b >= a * c:
        print(c)
    else:
        print(int(b/a))
    
if __name__ == '__main__':
    main()