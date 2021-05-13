S = input()

count = 0
black = 0
white = 0

for i in range(len(S)-1):
    if S[i] == 'B':
        black +=1
    else :
        white +=1
    if  S[i+1] == 'W':
        count += i+1 -white

print(count)