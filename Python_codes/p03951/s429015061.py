N = int(input())

S = input()
T = input()
x = 0
for i in range(N, 0, -1):
    if S[-i:] == T[:i]:
        x = i
        break
        
print(N*2-x)