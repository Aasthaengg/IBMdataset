import sys
S,T = input().split()
A,B = map(int,input().split())
U = input()

if not ( S.islower() and T.islower() and U.islower() ): sys.exit()
if not ( 1 <= len(S) <= 10 and 1 <= len(T) <= 10 ): sys.exit()
if not ( S != T ): sys.exit()
if not ( S == U or T == U ): sys.exit()
if not ( isinstance(A,int) and isinstance(B,int) ): sys.exit()

print(A-1,B,sep=' ') if U == S else print(A,B-1,sep=' ')