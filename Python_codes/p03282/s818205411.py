S = list(input())
K = int(input())

how_long_1 = 0
for i in range(len(S)):
    if S[i]=="1":
        how_long_1+=1
    else:
        break

if K > how_long_1:
    print(S[how_long_1])
else:
    print(1)
