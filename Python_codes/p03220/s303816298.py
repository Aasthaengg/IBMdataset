n=int(input())
t,a=map(int,input().split())
h=[int(_) for _ in input().split()]
h2=list(map(lambda x: abs(a-(t-x*0.006)), h))
print(h2.index(min(h2))+1)