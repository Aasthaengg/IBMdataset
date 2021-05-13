n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))

minus_index = -1
happy = 0

for i in range(n):
    index = a[i] - 1
    happy += b[index]
    if(a[i] == minus_index + 1):
        happy += c[minus_index-1]
    minus_index = a[i]

print(happy)