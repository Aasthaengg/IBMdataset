A,B,M = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

mini = min(a) + min(b)
for i in range(M):
    x,y,c = map(int,input().split())

    rei = a[x-1]
    den = b[y-1]
    coop = c

    if rei + den - coop < mini:
        mini = rei + den - coop

print(mini)