n = int(input())
a,b = map(int,input().split())
p = list(map(int,input().split()))

s = [0,0,0]

for i in p:
    if(i <= a):s[0] += 1
    elif(i <= b):s[1] += 1
    else:s[2] += 1
print(min(s))