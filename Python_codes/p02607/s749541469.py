n = int(input())

vec = [int(x) for x in input().split()]

cont = 0
for i in range(n):
    if (i+1)%2 != 0:
        if vec[i]%2 != 0:
            cont += 1;
        
print(cont)