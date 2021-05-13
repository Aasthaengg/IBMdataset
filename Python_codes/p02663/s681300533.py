h,m,H,M,K = map(int,input().split())
print(max(0,(H-h)*60+M-m -K))

