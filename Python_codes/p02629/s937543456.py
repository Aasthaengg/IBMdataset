def sep():
    return map(int,input().strip().split(" "))
def lis():
    return list(sep())

n=int(input())
k=n
s=""
while(k>0):
    t=k%26
    if t==0:
        t=26
        k-=26
    s+=chr(t+96)
    k//=26
print(s[::-1])
