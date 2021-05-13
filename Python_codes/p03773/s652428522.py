# A - Remaining Time 
def main():
    a, b = map(int, input().split())

    if a+b < 24:
        print(a+b)
    else:
        print(a+b-24)
        
if __name__ == '__main__':
    main()