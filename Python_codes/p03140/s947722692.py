n=int(input())
a=input()
b=input()
c=input()

diff_ch=[]
for i in range(n):
    diff_ch.append(len(set([a[i],b[i],c[i]]))-1)
print(sum(diff_ch))