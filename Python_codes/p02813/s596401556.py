import math
def count(N,i,li):
    a = 1
    for t in range(N):
        if li[t] == i:
            return a
        a += 1

N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
li1 = [i+1 for i in range(N)]
li2 = [i+1 for i in range(N)]
x = N-1
a_num = math.factorial(x) * (a[0]-1)
li1.remove(a[0])
b_num = math.factorial(x) * (b[0]-1)
li2.remove(b[0])
x -= 1

for i in range(1,N):
    a_num += math.factorial(x)*(count(N-i,a[i],li1)-1)
    li1.remove(a[i])
    b_num += math.factorial(x)*(count(N-i,b[i],li2)-1)
    li2.remove(b[i])
    x-=1
print(abs((a_num+1)-(b_num+1)))