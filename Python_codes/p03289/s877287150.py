S=input()
print('AC'if'A'in S and'C'in S[2:-1]and S[1:].replace('C','',1).islower()else'WA')