n = int(input())
lst = list(map(int,input().split()))

def pri(lst):
    for i in range(len(lst)-1):
        print(lst[i],end=" ")
    print(lst[-1])

pri(lst)
for i in range(1,n):
    v = lst[i]
    j = i-1
    while True:
        if j < 0:
            lst[0] = v
            break
        if lst[j] > v:
            lst[j+1] = lst[j]
            j -= 1
        else:
            lst[j+1] = v
            break
    pri(lst)

