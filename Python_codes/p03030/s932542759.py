n=int(input())
d=sorted(list(list(input().split())+[i+1] for i in range(n)),key=lambda x:(x[0],-int(x[1])))
for v in d:print(v[2])