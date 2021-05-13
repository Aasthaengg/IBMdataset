N = int(input())
if N == 0:
    print(2)
if N == 1:
    print(1)
else:
    li = [2,1]
    for i in range(2,N+1):
        li.append(li[i-2]+li[i-1])
        if i == N:
            print(li[i])