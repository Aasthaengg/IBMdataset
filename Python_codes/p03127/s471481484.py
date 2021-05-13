n = int(input())
ls = list(map(int,input().split()))
#a,bの最大公約数
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
#リスト l の最大公約数
def gcdlist(l):
    a = l[0]
    for i in range(len(l)):
        a = gcd(a,l[i])
    return a
print(gcdlist(ls))