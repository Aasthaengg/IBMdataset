n=int(input())
if n<1000:
    print(1000-n)
else:
    str1=""
    k=n//1000
    l=len(str(n))-len(str(k))
    str1=str(k)+'0'*l
    if str1==str(n):
        print(0)
    else:
        p=int(str1)+1000
        print(p-n)