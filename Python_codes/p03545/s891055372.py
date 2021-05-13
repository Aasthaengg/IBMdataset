A,B,C,D = (int(T) for T in list(input()))
ABCD = [A+B+C+D,A+B+C-D,A+B-C+D,A+B-C-D,A-B+C+D,A-B+C-D,A-B-C+D,A-B-C-D]
Op   = ['+++','++-','+-+','+--','-++','-+-','--+','---']
Disp = list(Op[ABCD.index(7)])
print('{}{}{}{}{}{}{}=7'.format(A,Disp[0],B,Disp[1],C,Disp[2],D))