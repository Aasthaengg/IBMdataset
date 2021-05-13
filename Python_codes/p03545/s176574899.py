S = input()
l = len(S)
ans = 0

for i in range(2**(l-1)):
    T = S[0]
    for j in range(l-1):
        if i>>j & 1:
            T = T + "-"
        else:
            T = T + "+"
        T = T+S[j+1]
    if eval(T) == 7:
        print(T+"=7")
        exit()