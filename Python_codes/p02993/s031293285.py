S = input()
Flag = True
for T in range(0,3):
    if S[T]==S[T+1]:
        Flag = False
        break
if Flag:
    print('Good')
else:
    print('Bad')