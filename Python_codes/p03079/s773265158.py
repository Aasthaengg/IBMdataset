def main():
    ls = [int(x) for x in input().split()]
    ls = set(ls)
    if len(ls)==1:
        print("Yes")
    else:
        print("No")
            
if __name__ == '__main__':
    main()