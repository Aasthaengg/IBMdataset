n = int(input())

divs = {}
ans = float('inf')

for i in range(1,int(n**(1/2))+1):
    if n%i == 0:
        a = i
        b = n//i
        tmp = a+b-2
        if tmp < ans:
            ans = tmp
print (ans)
