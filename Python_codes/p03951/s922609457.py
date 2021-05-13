N = int(input())
s = input()
t = input()

answer = 2*N

for x in range(1,N+1):
    if s[-x:] == t[:x]:
        answer = 2*N - x
        
print(answer)