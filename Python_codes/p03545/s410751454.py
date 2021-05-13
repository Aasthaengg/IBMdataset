import sys

*S, = input()

op = ['-', '+']
for i in op:
    for j in op:
        for k in op:
            e = f'{S[0]}{i}{S[1]}{j}{S[2]}{k}{S[3]}'
            if eval(e) == 7:
                print(f'{e}=7')
                sys.exit()