
n = int(input())

ans = 0

a = 1

while a <= n:
 
    if a == 1 :
        ans =  ans + (n - 1)
    else :
        if n % a == 0 :
            ans = ans + ( (n // a) - 1)
        else :
            ans = ans + ( (n // a) )

    a += 1

print(ans)