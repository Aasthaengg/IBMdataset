from collections import Counter
def main():
    n=int(input())
    a=Counter(map(int,input().split()))
    d=0
    for k,v in a.items():
        if k > v:
            d += v
        elif k < v:
            d += v-k
    print(d)

if __name__ == "__main__":
    main()