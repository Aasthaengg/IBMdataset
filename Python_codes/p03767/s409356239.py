N=int(input())
als=input().split()
al=[ int(v) for v in als ]
al.sort(reverse=True)

s=0
for i in range (N):
   s+=al[ 2*i +1]

print(s)