is_prime = [1]*101010
is_prime[0] = 0
is_prime[1] = 0
max = 101010

for i in range(2,max):
    if is_prime[i]:
        j = i*2
        while j <= max-1:
            is_prime[j] = 0
            j += i

a = [0]*max
for i in range(max):
    if(i%2==0): 
        continue
    if(is_prime[i]==1 and is_prime[(i+1)//2]==1):
        a[i]=1

s = [0]*(max+1)
for i in range(max):
    s[i+1] = s[i]+a[i]


q = int(input())
for i in range(q):
    l, r = map(int, input().split())
    r += 1
    
    print(s[r]-s[l])