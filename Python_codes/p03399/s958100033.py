#n = int(input())
#a,b = map(int,input().split())
#a_L = list(map(int,input().split()))
a_L = []
for _ in range(4):
    a_L.append(int(input()))
print(min(a_L[0],a_L[1])+min(a_L[2],a_L[3]))