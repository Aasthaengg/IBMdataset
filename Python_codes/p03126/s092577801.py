# その23
# ABC118 B - Foods Loved by Everyone

n,m = map(int,input().split())
K_2=[]
t = 0
for i in range(n):
    A, *K =list(map(int,input().split()))
    K_2 +=K
K_3 = list(set(K_2))
for j in range(len(K_3)):
    K_4 = K_2.count(K_3[j])
    if K_4 == n:
        t +=1
print(t)