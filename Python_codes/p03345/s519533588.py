A,B,C,K = map(int,input().split())

if K%2 == 0:
    ans = A-B
    print(ans) if abs(ans)<10**18 else print("Unfair")
else:
    ans = B-A
    print(ans) if abs(ans)<10**18 else print("Unfair")