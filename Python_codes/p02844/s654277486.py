from math import ceil
N = int(input())
S = input()
ans = [0]*1000
one = [0]*10
two = [0]*100

for s in S:
    s = int(s)
    for i in range(10):
        for j in range(10):
            if two[i*10+j]//1:
                ans[i*100+j*10+s] = 1 
            else:
                if one[i]//1 and two[i*10+s] == 0:
                    two[i*10+s] = 0.5
                elif one[s] == 0:
                    one[s] = 0.5        
    one = list(map(lambda x: ceil(x), one))
    two = list(map(lambda x: ceil(x), two))

print(sum(ans))