S = str(input())
L = []

for i in range(len(S)):
    try:
        L.append(abs(int(S[i]+S[i+1]+S[i+2])-753)) 
    except:
        break

print(min(L))