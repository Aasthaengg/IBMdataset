s = list(map(int, input().split()))
for i in range(1,s[0]+1):
    a=i*(i+1)/2
    if a>=s[0]:
        print(i)
        break