a,b=map(int,input().split())
a_l=[]
for i in range(b-a):
            a_l.append(i)
            i=i+1

print(sum(a_l)-a)

