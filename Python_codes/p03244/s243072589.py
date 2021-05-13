from collections import Counter
n = int(input())
l = list(map(int,input().split()))
odd = []
even = []
for i in range(n//2):
    odd.append(l[2*i])
    even.append(l[2*i+1])
c_odd = list(Counter(odd).items()) + [(-1,0)]
c_even = list(Counter(even).items()) + [(-1,0)]
c_odd = sorted(c_odd, key=lambda x:-x[1])
c_even = sorted(c_even, key=lambda x:-x[1])

c_odd = c_odd[:2]
c_even = c_even[:2]
# print(c_odd,c_even)

if c_odd[0][0] != c_even[0][0]:
    print(n-c_odd[0][1]-c_even[0][1])
    exit()
else:
    print(n-c_odd[0][1]-max(c_odd[1][1],c_even[1][1]))