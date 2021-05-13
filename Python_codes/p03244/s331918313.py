from collections import Counter
def main():
    n=int(input())
    v=list(map(int,input().split()))
    v0=Counter(v[0::2]).most_common(2)
    v1=Counter(v[1::2]).most_common(2)
    
    if v0[0][0] != v1[0][0]:
        print(n - v0[0][1] - v1[0][1])
    else:
        if len(v0) == 1 and len(v1) == 1:
            print(n//2)
        else:
            print(n-max(v0[0][1]+v1[1][1], v0[1][1]+v1[0][1]))
    
if __name__ == "__main__":
    main()