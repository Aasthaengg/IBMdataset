S=list(str(input()))
for i in range(1,4):
    if S[i-1]==S[i]:
        print('Bad') 
        exit()

print('Good')