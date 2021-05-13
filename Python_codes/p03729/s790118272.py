A,B,C= input().split()
a=str(A)
b=str(B)
c=str(C)
if a[-1]==b[0]:
    if b[-1]==c[0]:
        print("YES")
        exit()
print("NO")