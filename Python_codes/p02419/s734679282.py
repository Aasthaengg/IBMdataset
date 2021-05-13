W = input().lower()
T=[]
t = input()
while t != "END_OF_TEXT":
 t = t.lower().split()
 T += t
 t = input()

print(T.count(W))