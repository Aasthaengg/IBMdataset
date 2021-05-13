s = int(input())

def f(n):
    if n%2 == 0:
        return int(n/2)
    else:
        return 3*n+1
    
memo = {i: 0 for i in range(1, 999999)}

a = s
i = 1
memo[a] = 1

while(True):
    i += 1
    a = f(a)

    if memo[a]:
        break

    memo[a] = 1
    
        
print(i)