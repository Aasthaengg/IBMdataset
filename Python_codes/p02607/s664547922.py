n=input()
va=list(map(int,input().split()))
print(sum(a%2 for a in va[::2]))