def main():
    *a, = map(int, open(0).read().split())
    print(sum(a[1:])-a[0])
if __name__=="__main__":
    main()