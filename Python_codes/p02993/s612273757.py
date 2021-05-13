# ABC131
# A Security
S  = input()
sl = len(S)
for i in range(sl-1):
    if S[i] == S[i+1]:
        print('Bad')
        exit()
print('Good')
