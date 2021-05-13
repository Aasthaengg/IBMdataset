n = int(input())

def dig(num):
    ans = 0
    while num>0:
        ans += num%10
        num//=10
    return ans

mi = float('inf')
for i in range(1,n//2+1):
    a = dig(i)+dig(n-i)
    mi = min(a,mi)
print(mi)
