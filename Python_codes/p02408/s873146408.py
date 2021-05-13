epochs = int(input())
patterns = ['S', 'H', 'C', 'D']
checker = {pattern: [True]*13 for pattern in patterns}
for i in range(epochs):
    pattern, num = input().split()
    num = int(num)
    checker[pattern][num-1] = False
 
for pattern in patterns:
    for i in range(13):
        if checker[pattern][i]:
            print(pattern, i+1)