N = int(input())
print(0)
while True:
    x = input().strip()
    if x=="Vacant":break
    high = N
    low = 0
    while high-low>1:
        mid = (high+low)//2
        print(mid)
        y = input().strip()
        if x=="Vacant":break
        if (mid%2==0 and y==x) or (mid%2==1 and y!=x):
            low = mid
        else:
            high = mid