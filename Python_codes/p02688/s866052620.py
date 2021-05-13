n,k = map(int,input().split())
sunuke = [0]*n

for i in range(k):
    input()
    for j in map(int,input().split()):
        sunuke[j-1] += 1

print(sunuke.count(0))