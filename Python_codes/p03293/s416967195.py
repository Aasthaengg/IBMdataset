S = input()
T = input()

T = T+T

for i in range(0,len(T),1):
    if S == T[i:len(S)+i]:
        print("Yes")
        exit()
print("No")