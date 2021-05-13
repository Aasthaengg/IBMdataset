N,A,B = map(int,input().split())
l = list(range(1,N+1))
su = 0
for i in l:
    num_li = (list(str(i)))
    num_li = list(map(int,num_li))
    k = sum(num_li)
    if A <= k <= B:su+=i
print(su)