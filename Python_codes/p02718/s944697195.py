n,m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
a_sum=sum(a)
for i in range(1,m+1):
    if a[-i]<a_sum*(1/(4*m)):
        print("No")
        exit()
print("Yes")
