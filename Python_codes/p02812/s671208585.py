n = int(input())
S = input()
count = 0
for i in range(n-2):
    if S[i] +S[i+1] + S[i+2] == 'ABC':
        count +=1
print(count)