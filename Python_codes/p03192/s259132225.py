import sys

a = list(input())

cnt = 0
for i in range(len(a)) :
    if a[i] == '2':
        cnt +=1

print(cnt)