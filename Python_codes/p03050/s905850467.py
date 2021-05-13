n=int(input())
p=0
for i in range(1,int(n**0.5)+10):
    if n%i==0 and n//i-1>i:
        p+=n//i-1
print(p)