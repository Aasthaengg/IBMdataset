inp = list(map(int,input().split()))
n = inp[0]
k = inp[1]

n -= k
count = 1

while(n != 0):
    n -= 1
    count += 1

print(count)