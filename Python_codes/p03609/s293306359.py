def main():
    x,t = (int(x) for x in input().split())
    if x <= t: print(0)
    else: print(x-t)

if __name__ == '__main__':
    main()