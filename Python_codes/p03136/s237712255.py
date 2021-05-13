N = int(input())
L = list(map(int,input().split()))

if 2*max(L)<sum(L):
    print("Yes")
else:
    print("No")