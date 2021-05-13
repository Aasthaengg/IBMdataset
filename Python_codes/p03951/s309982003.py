n = int(input()) 
S = input()
T = input()
ans = 0
for i in range(n):
    if S[i:] == T[:n-i]:
        print(n-i+i*2)
        break
else:
    print(2*n)