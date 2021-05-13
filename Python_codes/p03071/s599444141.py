# input
A, B = map(int, input().split())

# check
coins = 0
for n in range(2):
    if A > B:
        coins += A
        A -= 1
    else:
        coins += B
        B -= 1
        
print(coins)
