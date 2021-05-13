
N = int(input())
m = [input() for _ in range(2)]

i = 0
count = 0
prestate = -1
while i < N:
    if i == 0:
        if m[0][0] != m[1][0]:
            count = 6
            prestate = 0
            i += 2
        else:
            count = 3
            prestate = 1
            i += 1
    else:
        if m[0][i] == m[1][i]: 
            if prestate == 1:
                count *= 2
                count %= int(1e9+7)
            i += 1
            prestate = 1
        else:
            if prestate == 0:
                count *= 3
            else:
                count *= 2
            count %= int(1e9+7)
            i += 2
            prestate = 0
            
print(count)