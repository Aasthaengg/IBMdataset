s = int(input())
a = [s]
ans = 1
n = s
while 1:
    if n%2 == 0:
        n = n//2
    else:
        n = n*3 + 1
    if n in a: 
        ans += 1
        break
    a.append(n)
    ans += 1

print(ans)


