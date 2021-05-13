N=int(input())
A=list(map(int,input().split()))
print("YES" if not sum(A)%2 else "NO")
