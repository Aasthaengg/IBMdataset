A,B = map(int,input().split())
ans  = 1
for i in range(0,20):
    if ans >= B:
        print(i)
        exit()
    else:
        ans += (A-1)  