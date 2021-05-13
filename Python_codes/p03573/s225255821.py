def main():
    abc = input().split()
    n = [int(x) for x in abc if abc.count(x)==1]
    print(n[0])

if __name__ == '__main__':
    main()