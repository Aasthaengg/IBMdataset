n = int(input())
list = [int(input()) for _ in range(n)]

link = [0] * ( n + 1)
for i in range(n):
    link[ list[i]] = link[list[i] -1] + 1
print( n - max(link)) 