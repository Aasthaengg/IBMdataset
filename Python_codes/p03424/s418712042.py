n=int(input())
s=set()
l=input().split()
for i in l:
    s.add(i)
if(len(s)==3):
    print('Three')
else:
    print('Four')
