def odd():
    for i in range(M):
        print(order[i], reverse[i])

def multipule4():
    d = 0
    for i in range(M):
        if reverse[i] - order[i] == N//2:
            d = 1
        print(order[i+d], reverse[i])

def even():
    d = 0
    for i in range(M):
        if i == (N//2-1) //2:
            d = 1
        print(order[i+d], reverse[i])
    

N, M = map(int, input().split())
order = [i for i in range(2, N+1)]
reverse = order[::-1]

if N%2 != 0:
    odd()
elif N%4 == 0:
    multipule4()
else:
    even()