A,B,C = map(int,input().split())
K = int(input())

flag = "No"
for x in range(K+1):
    for y in range(K+1):
        for z in range(K+1):
            if x + y + z <= K and A*(2**x) < B*(2**y) and B*(2**y) < C*(2**z):
                flag = "Yes"
print(flag)