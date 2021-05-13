S = input()
for i in range(len(S) - 1):
    if S[i:i+2].count(S[i]) == 2:
        print('Bad')
        break
else:
    print('Good')
