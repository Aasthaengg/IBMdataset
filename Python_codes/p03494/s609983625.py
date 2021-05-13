N=int(input())
a=input().split()
a_int = [int(i) for i in a]

count=0
while 1:
    k=0
    for i in a_int:
        k = k + i%2
    if k == 0:
        a_int = [i/2 for i in a_int]
        count=count+1
    else:
        print(count)
        break
