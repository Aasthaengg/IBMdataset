n,b,r = map(int, input().split())
print(b*(n//(b+r)) + min(b,n%(b+r)))