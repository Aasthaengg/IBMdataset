import itertools
def main():
    a=list(map(int,input().split()))
    for i in a:
        if i%2==0:
            print(0)
            return
    ans = float("inf")
    for x in itertools.combinations(a, 2):
        d = 1
        for y in x:
            d *= y
        ans = min(ans, d)
    print(ans)
    
if __name__ == "__main__":
    main()