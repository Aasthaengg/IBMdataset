n = int(input())
l = list(map(int,input().split()))
l.sort()

k_1 = l[(n//2)-1]
k_2 = l[(n//2)]
print(k_2-k_1)