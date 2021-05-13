o=input()
e=input()
a=""
for i in range(len(e)):
    a+=o[i]+e[i]
if len(o)-len(e)==1:
    a+=o[-1]
print(a)