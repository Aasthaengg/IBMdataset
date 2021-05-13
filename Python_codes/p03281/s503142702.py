n = int(input())

def divs(n:int):
    divs = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divs.append(i)
            if i != n // i:
                divs.append(n//i)
    return len(divs)

ans = 0
for i in range(1,n+1,2):
    if divs(i) == 8:
        ans += 1

print (ans)
