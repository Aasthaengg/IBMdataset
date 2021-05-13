N=int(input())
A,B=map(int,input().split())
P=list(map(int,input().split()))

p1=[i for i in P if i <= A]
p2=[i for i in P if A+1<= i <=B]
p3=[i for i in P if i >= B+1]

print(min([len(p1),len(p2),len(p3)]))