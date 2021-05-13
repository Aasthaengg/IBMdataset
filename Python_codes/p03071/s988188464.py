def mi(): return map(int,input().split())
def lmi(): return list(map(int,input().split()))
def ii(): return int(input())
def isp(): return input().split()

a,b=mi()
ans=max(a+a-1,a+b)
ansans=max(ans,b+b-1)
print(ansans)