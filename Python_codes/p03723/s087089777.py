def main():
    a=tuple(map(int,input().split()))
    e=set()
    while a not in e:
        for x in a:
            if x % 2 != 0:
                print(len(e))
                return
        e.add(a)
        a=((a[1]+a[2])//2,(a[0]+a[2])//2,(a[0]+a[1])//2)
    else:
        print(-1)
    
if __name__ == "__main__":
    main()