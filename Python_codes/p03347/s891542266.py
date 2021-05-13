n = int(input())
a = [int(input()) for i in range(n)]
def check():
    globals()
    s = 0
    if a[0]!=0:
        return -1
    for i in range(n-1):
        if a[i+1]<=a[i]:
            s+=a[i]
        if a[i+1]>a[i]+1:
            return -1
    return s+a[-1]
print(check())