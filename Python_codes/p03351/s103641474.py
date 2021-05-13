

def main():
    a,b,c,d = map(int, input().split())
    if abs(c-a) <= d:
        print('Yes')
    elif abs(c-b) <= d and abs(b-a) <= d:
        print('Yes')
    else:
        print('No')

    

if __name__ == "__main__":
    main()
