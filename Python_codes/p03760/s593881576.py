O = input()
E = input()

K = len(E)

String = ""

for i in range(K):
    
    String += O[i]
    String += E[i]

if len(O)>len(E):
    String += O[-1]

print(String)