
n = int(input())
x = list(map(int,input().split()))

count = 0
while True:
    if [i for i in x if i % 2 == 1]:
        break
    x = [i/2 for i in x]
    count+=1

print(count)