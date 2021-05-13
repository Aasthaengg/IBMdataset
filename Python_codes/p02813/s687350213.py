N=int(input())
import itertools

l=[i for i in range(1,N+1)]
li=[]
for v in itertools.permutations(l,N):
    li.append(list(v))
a=li.index(list(map(int,input().split())))
b=li.index(list(map(int,input().split())))

print(abs(b-a))
