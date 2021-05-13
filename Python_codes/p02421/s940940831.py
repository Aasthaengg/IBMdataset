x = int(input())
T = 0
H = 0
for i in range(x):
    a,b = map(str,input().split())
    if a < b:
        H+=3
    elif a == b:
        T+=1
        H+=1
    else:
        T+=3

print(T,H)
