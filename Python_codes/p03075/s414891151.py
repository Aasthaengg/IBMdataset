a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
k = int(input())
print(":(" if max(a,b,c,d,e) - min(a,b,c,d,e) > k else "Yay!")