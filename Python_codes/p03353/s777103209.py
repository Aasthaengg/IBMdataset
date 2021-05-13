s=input()
K=int(input())
x=[]
for i in range(5):
  x.extend(list({s[j:j+i+1] for j in range(len(s)-i)}))
x=sorted(x)
print(x[K-1])