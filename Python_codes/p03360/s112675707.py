ls = list(map(int,input().split()))
K = int(input())
ls.sort()
ans = ls[0]+ls[1]+ls[2]*2**K
print(ans)