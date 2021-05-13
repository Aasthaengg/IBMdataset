k,x=map(int, input().split())

k_min=x-k+1
k_max=x+k-1

k_list=[str(i) for i in range(k_min, k_max+1)]

print(" ".join(k_list))