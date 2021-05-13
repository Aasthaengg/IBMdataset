n=int(input())
rec=list(map(int,input().split()))
s=[0,abs(rec[1]-rec[0])]
for i in range(2,n):
        total2=abs(rec[i]-rec[i-2])+s[i-2]
        total1=abs(rec[i]-rec[i-1])+s[i-1]
        s.append(min(total2,total1))
print(s[-1])