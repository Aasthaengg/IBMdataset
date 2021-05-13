n = int(input())
data = []
for i in range(n) :
    s, p = input().split()
    data.append([s, int(p), i+1])

data.sort(key = lambda x:x[1], reverse=True)
data.sort(key = lambda x:x[0])

for num in data:
    print(num[2])
