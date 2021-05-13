N = int(input())
T,A = map(int,input().split())
H = list(map(int,input().split()))
d = {}
for x in H:
    d[x] = abs(A-(T-x*0.006))
counter = 1
counter_x = 1
min_ = 100000
for i in d.values():
    if(min_>=i):
        min_ = i
        counter_x = counter
    counter += 1
print(counter_x)