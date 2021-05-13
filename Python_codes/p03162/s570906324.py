n = int(input())
a,b,c = map(int,input().split())
for i in range(1,n):
    aa,bb,cc = map(int,input().split())
    aaa,bbb,ccc = a,b,c
    a = max(aa+bbb,aa+ccc)
    b = max(bb+ccc,bb+aaa)
    c = max(cc+aaa,cc+bbb)
print(max(a,b,c))