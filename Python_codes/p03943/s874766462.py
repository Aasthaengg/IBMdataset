a,b,c = (map(int, input().split()))
s1 = a+b
s2 = b+c
s3 = c+a
if s1==c or s2==a or s3==b:
    print("Yes")
else:
    print("No")
         
