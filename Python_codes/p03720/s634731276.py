a,b = map(int,input().split())
array = [list(map(int,input().split())) for i in range(b)]
count = [0]*a
for i in range(a):
    for j in range(b):
        if i+1 in array[j]:
            count[i] += 1
for i in range(a):
    print(count[i])