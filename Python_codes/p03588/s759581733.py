a = int(input())
l = []
for i in range(a):
    ta,tb = map(int,input().split())
    l.append([ta,tb])
l.sort()

ans =0
A = 1
B = 10000000010
for i , j in l:
    ans+= min(i-A,abs(B-j))
    A = i;B=j
    # print(ans)
print(ans+l[-1][1]+1)