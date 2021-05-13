N,X = map(int,input().split())
l = list(map(int,input().split()))
p = 0
count = 1

for i in l:
    p += i
    count += 1
    if p > X:
        count -= 1
        break
print(count)