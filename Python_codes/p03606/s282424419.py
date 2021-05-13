N = int(input())
a = []

for i in range(N):
    x,b = map(int,input().split())
    sa = b-x+1
    a.append(sa)
    

print(sum(a))