 
def main():
    N = int(input())
    A = list(map(int,input().split()))

    ans=0
    maximum=0
    
    for a in A:
        ans += max(0,maximum-a)
        maximum=max(maximum,a)

    print(ans)
        
if __name__ == '__main__':
    main()