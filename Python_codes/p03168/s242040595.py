n = input()
n = int(n)
p = list(map(float,input().split()))

l = [1]

for i in range(n):
    t1 = [j*(1-p[i]) for j in l]
    t1.append(0)
    t2 = [0]+[j*p[i] for j in l]
    l = [t1[j] + t2[j] for j in range(len(t1))]

l.reverse()
print(sum([l[i] for i in range((n+1)//2)]))
