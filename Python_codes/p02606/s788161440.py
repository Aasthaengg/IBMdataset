ijyou,ika,sr = map(int,input().split())

count= 0

for i in range(ijyou,ika+1):
    if i % sr == 0:
        count += 1

print(count)