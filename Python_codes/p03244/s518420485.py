from collections import Counter
def main():
    n=int(input())
    v=list(map(int,input().split()))
    v0=sorted(Counter(v[::2]).items(), key=lambda x: x[1])
    v1=sorted(Counter(v[1::2]).items(), key=lambda x: x[1])
    
    if v0[-1][0] != v1[-1][0]:
        print(n-v0[-1][1]-v1[-1][1])
    else:
        if len(v0) == 1 and len(v1) == 1:
            print(n//2)
        else:
            a = (v0[-1][1] + v1[-2][1]) if len(v1) > 1 else 0
            b = (v0[-2][1] + v1[-1][1]) if len(v0) > 1 else 0
            print(n - max(a, b))
    
if __name__ == "__main__":
    main()