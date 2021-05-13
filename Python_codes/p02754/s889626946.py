N,A,B = map(int,input().split())
#Aが青
#Bが赤
i = N // (A+B)
b = i*A
t = N % (A+B)
if t > A:
   t = A
print(b+t)