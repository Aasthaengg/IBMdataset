N=int(input())
a=list(map(int,input().split()))

print([abs(ai-sum(a)/N) for ai in a].index(min([abs(ai-sum(a)/N) for ai in a])))