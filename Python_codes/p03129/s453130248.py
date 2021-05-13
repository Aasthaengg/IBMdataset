A,B = list(map(int,input().split()))
ans = (A-1) // 2+1
if ans >= B:
    print("YES")
else:
    print("NO")