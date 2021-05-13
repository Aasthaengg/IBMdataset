#39
import copy
N = int(input())
a = []
for i in range(N):
    a.append(int(input()))
    
Max = max(a)
b = copy.copy(a)
b.remove(Max)
sub = max(b)

for i in a:
    if i !=Max:
        print(Max)
    else:
        print(sub)