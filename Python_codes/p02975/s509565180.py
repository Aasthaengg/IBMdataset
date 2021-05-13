from collections import Counter
n = int(input())
a = list(map(int, input().split()))
b = Counter(a)
c = list(b.items())
if all(i==0 for i in a):
    print("Yes")
elif len(b)==2 and n%3==0 and b[0]==n//3:
    print("Yes")
elif len(b)==3 and c[0][0]^c[1][0]^c[2][0]==0 and c[0][1]==c[1][1]==c[2][1]:
    print("Yes")
else:
    print("No") 