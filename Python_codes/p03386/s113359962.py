A,B,K = list(map(int,input().split()))
s = set()
for i in range(0,K):
    s.add(A+i)
for i in range(0,K):
    s.add(B-i)
l = sorted(filter(lambda x: A <= x <=B,list(s)))
for i in l:
    print(i)