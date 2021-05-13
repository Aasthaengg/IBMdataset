a,b,k=map(int,input().split())
if k<a:
    print(a-k, b)
elif a<=k<=a+b:
    print("0", b-(k-a))
elif a+b<k:
    print("0", "0")
