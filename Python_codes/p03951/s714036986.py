N = int(input())
S = input()
T = input()
if S == T:
    print(len(S))
    exit()
for i in range(len(T)):
    tmp = S+''.join(T[-i-1:])
    if tmp[i+1:] == T:
        print(len(tmp))
        exit()  