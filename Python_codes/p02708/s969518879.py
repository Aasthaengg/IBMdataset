n,k = map(int,input().split())

num = 0

for i in range(k,n+2):
    num += n * i - (i/2) *(i -1) - ((i-1)/2 * i) +  1

print(int(num) %( 10**9 + 7))

