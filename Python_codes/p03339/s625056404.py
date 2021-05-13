N = int(input())
S = input()
 
eastNumber = S.count('E')
westNumber = 0
minimum = N
 
for i in range(N):
    if S[i] == 'E':
        eastNumber -= 1
        number = eastNumber + westNumber
        if minimum > number:
            minimum = number
    else:
        number = eastNumber + westNumber
        if minimum > number:
            minimum = number
        westNumber += 1
 
print(minimum)