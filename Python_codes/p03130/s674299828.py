li = [0,0,0,0]

for i in range(3):
    a,b = map(int,input().split())
    for j in range(1,5):
        if(a == j or b == j):
            li[j-1] += 1;

if(min(li) == 0 or max(li) == 3):
    print("NO")
else:
    print("YES")