def is_prime(n):
    i=2
    while i*i<=n:
        if n%i==0:
            return False
        i+=1
    return True
    
s=[]
for _ in range(int(input())):
    s.append(is_prime(int(input())))
print(sum(s))

