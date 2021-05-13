n = int(input())

al = list(map(int, input().split())) 

res = 0
for i in range(n):
    j = al[i]
    while j % 2 ==0:
        res +=1
        j = j//2

print(res)