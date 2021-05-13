N = int(input())
l = list(map(int, input().split()))

counter = 0

for i in range(N):
    if l[l[i]-1] == i+1:
        counter += 1
        l[i] = -99
print(counter)
