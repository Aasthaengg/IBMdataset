N = int(input())
S = input()
count = 0
for i in range(0,N-1):
    if S[i:i+3] == 'ABC':
        count += 1
print(count)