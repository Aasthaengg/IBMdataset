S=input()
w=int(input())
Sdash=[]
a=''
for i in range(0,len(S)//w):
    Sdash.append(S[w*i:w*(i+1)])
if len(S)%w!=0:
    Sdash.append(S[((len(S)//w)*w):])
for i in range(len(Sdash)):
    a+=Sdash[i][0]
print(a)