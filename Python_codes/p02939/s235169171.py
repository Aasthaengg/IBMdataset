S=input()
A=[""]
a=""
for s in S:
    if a+s!=A[-1]:
        A.append(a+s)
        a=""
    else:
        a+=s
print(len(A)-1)