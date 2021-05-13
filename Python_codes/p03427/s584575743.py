N = input()

Nl = len(N)
tmp = N[0] + '9'*(Nl-1)

if int(N) >= int(tmp):
    answer = int(N[0]) + 9*(Nl-1)
else:
    answer = int(N[0])-1 + 9*(Nl-1)
    
print(answer)