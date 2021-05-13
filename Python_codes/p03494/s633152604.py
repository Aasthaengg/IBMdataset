n = int(input())
l = list(map(int,input().split()))
count = 0
while all(l[i] % 2 == 0 for i in range(n)):
    l = [l[i] / 2 for i in range(n)]
    count += 1
    
print(count)