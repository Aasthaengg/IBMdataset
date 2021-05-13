n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))
count = 0
bonus = 0
for i in a:
    count += b[i-1]
    if i == bonus:
        count += c[i-2]
    bonus = i+1
print(count)