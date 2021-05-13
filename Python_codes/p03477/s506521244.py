A,B,C,D = (int(T) for T in input().split())
L = A+B
R = C+D
print(['Balanced','Left','Right'][(L!=R)+(L<R)])