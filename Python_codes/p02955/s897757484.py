def divisor(n): #約数全列挙
    ans = [1,n]
    i = 2
    while i**2 <= n:
        if n%i == 0:
            ans.append(i)
            if i**2 < n:
                ans.append(n//i)
        i += 1
    ans.sort()
    return ans

n,k = map(int,input().split())
A = list(map(int,input().split()))
d_max= sum(A)
div = divisor(d_max)[::-1]

for ans in div:
    b = [a%ans for a in A]
    b.sort()
    s = sum(b)
    if sum(b[:-s//ans]) <=k:
        print(ans)
        exit()