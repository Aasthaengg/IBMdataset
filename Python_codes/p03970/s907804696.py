A = "CODEFESTIVAL2016"
S = [i for i in input()]
A = [i for i in A]
count=0
for (s,a) in zip(S,A):
    if s!=a:
       count+=1
print(count)