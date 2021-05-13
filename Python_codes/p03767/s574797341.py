N = int(input())
l = list(map(int,input().split()))
l.sort(reverse = True )
sum = 0
for i in range(1,2*N,2):
    sum += l[i]
print(sum)
