N = int(input())
a = list(map(int, input().split()))

a_max = max(a)
a_min = min(a)

if a_max >= abs(a_min):
    flag = True
    index = a.index(a_max)
else:
    flag = False
    index = a.index(a_min)

m = 2 * N -2
print (m)

count = 0
for i in range(N):
    if i != index:
        print (index+1, i+1)
        count += 1

if flag: #全て非負の数になっている時
    for i in range(N-1):
        print (i+1, i+2)
        count += 1
else:
    for i in range(N-1,0,-1):
        print (i+1, i)
        count += 1

# print (m == count)