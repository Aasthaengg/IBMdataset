
n=int(input())
t,a=map(int,input().strip().split(" "))
ar=[abs(t-(0.006*(int(i)))-a) for i in input().strip().split(" ")]
k=min(ar)
print(ar.index(k)+1)