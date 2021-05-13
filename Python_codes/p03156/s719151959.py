n = int(input())
a,b = map(int,input().split())
p = list(map(int,input().split()))

res = [0]*3

for v in p:
    if v <= a:
        res[0]+=1
    elif a < v <= b:
        res[1]+=1
    else:
        res[2]+=1
print(min(res))