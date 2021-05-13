N = int(input())
T = list(map(int,input().split()))
S = 0
for i in range(len(T)):
    list.sort(T, reverse=False)
    S = (T[0]+T[1])/2
    T.append(S)    
    T.pop(0)
    T.pop(0)
    
    if len(T) ==1:break
print(T[0])