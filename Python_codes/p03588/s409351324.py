n = input()

a = []
b = []

count = 0

for i in range(n):
    a_,b_ =[int(i) for i in raw_input().split()]
    a.append(a_)
    b.append(b_)
    

c = zip(a,b)
c.sort()
a, b = zip(*c)
a = list(a)
b = list(b)

before_rank = 1
before_score = 10000000000
for i in range(n):

    count += min(a[i]-before_rank, before_score-b[i])
    before_rank = a[i]
    before_score = b[i]

count += before_score + 1


print(count)
