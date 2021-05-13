NK = [int(i) for i in input().split(' ')]
p=[int(i) for i in input().split(' ')]
p.sort()
S=sum(p[0:NK[1]])
print(S)