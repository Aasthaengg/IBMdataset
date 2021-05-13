N = int(input())
l = list(map(int,input().split()))
l.sort(reverse=True)

al=list()
bl=list()

i = 0
j = 0
while 2*i < N:
    al.append(l[2*i])
    i = i + 1
while 2*j+1 < N:
    bl.append(l[2*j+1])
    j = j+1
    
print(sum(al)-sum(bl))