n = int(input())
k = int(input())
x = []
for i in range(n+1):
     x.append((1*(2**i))+k*(n-i))
     x.append((1+k*i)*(2**(n-i)))
print(min(x))