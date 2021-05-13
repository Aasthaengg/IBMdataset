n,k = list(map(int, input().split()))

sunuke = [1] * n
 
for i in range(k):
    d = int(input())
    a = list(map(int, input().split()))
    for j in a:
        sunuke[j-1] = 0

print(sum(sunuke))