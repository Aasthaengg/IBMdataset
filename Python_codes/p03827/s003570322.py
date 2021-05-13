N = int(input())
S = input()

x = 0
temp = 0
for n in range(N):
    if S[n]=='I':
        temp+=1
    elif S[n]=='D':
        temp-=1
    if temp > x:
        x = temp
print(x)