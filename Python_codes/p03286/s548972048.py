n=int(input())
s=""
while n!=0:
    s+=str(abs(n%(-2)))
    n=(n-n%2)//(-2)
print(s[::-1] if s else 0)
