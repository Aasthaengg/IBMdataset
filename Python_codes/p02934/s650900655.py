n =  int(input())
a =list(map(int,input().split()))
rev_a=[]
b=0
       

for i in a:
    j = 1 / i
    rev_a.append(j)
b=0
for k in rev_a:
    b += k

print(1/b)