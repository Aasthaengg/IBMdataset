N=int(input())
a = [int(i) for i in input().split()]

count=0
while 1:
    if sum([i%2 for i in a]) == 0:
        a = [i/2 for i in a]
        count=count+1
    else:
        print(count)
        break
