k = int(input())

maxV = (10**6)**2

i = 0
sevens = 0
while i < 10**6+1:
    sevens = sevens * 10 + 7
    sevens = sevens % k
    i+=1
    if sevens % k == 0:
        print(i)
        exit()

print(-1)