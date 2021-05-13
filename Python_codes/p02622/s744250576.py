S = list(input())
T = list(input())

length = int(len(S))
difference = 0

for i in range(length):
    if S[i] != T[i]:
        difference = difference + 1

   
print(str(difference))