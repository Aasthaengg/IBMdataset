#nの約数列挙
def divisor(n):
    ass = []
    for i in range(1,int(n**0.5)+1):
        if n%i == 0:
            ass.append(i)
            if i**2 == n:
                continue
            ass.append(n//i)
    ass.sort()
    return ass

n = int(input())

li = divisor(n)

l = len(li)

if l%2 == 1:
    ans = li[l//2] * 2 -2
else:
    ans = li[(len(li)//2)] + li[(len(li)//2)-1] - 2

print(ans)