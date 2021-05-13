n,m = map(int,raw_input().split())
for i in range(0,n):
    if i == 0:
        matrix = [map(int,raw_input().split())]
    else:
        matrix.append(map(int,raw_input().split()))
vec=[]
for j in range(0,m):
    vec.append(raw_input())
mul = []
for k in range(0,n):
    num_sum=0
    for l in range(0,m):
        num_sum += matrix[k][l] * int(vec[l])
    print num_sum

